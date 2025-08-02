_U='dataIfGroupVer1'
_T='dataIfT38BasePort'
_S='dataIfT38NoSignalTimeout'
_R='dataIfT38NoSignalEnable'
_Q='dataIfT38FinalFramesRedundancy'
_P='dataIfCodecT38ProtectionLevel'
_O='dataIfClearChannelCodecPreferred'
_N='dataIfCodecMediaTypeImageEnable'
_M='dataIfCodecT38Enable'
_L='dataIfAnalogCedDetectionBehavior'
_K='dataIfCedFaxToneEnable'
_J='dataIfCngToneDetectionEnable'
_I='disable'
_H='ifIndex'
_G='IF-MIB'
_F='MxEnableState'
_E='Unsigned32'
_D='Integer32'
_C='read-write'
_B='MX-DATAIF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_G,_H)
mediatrixConfig,=mibBuilder.importSymbols('MX-SMI','mediatrixConfig')
MxEnableState,=mibBuilder.importSymbols('MX-TC',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
dataIfMIB=ModuleIdentity((1,3,6,1,4,1,4935,15,35))
if mibBuilder.loadTexts:dataIfMIB.setRevisions(('2010-02-16 00:00','2009-09-10 00:00','2009-06-12 00:00','2005-05-10 00:00','2005-04-29 00:00','2005-04-28 00:00','2005-04-19 00:00','2005-03-17 00:00','2005-03-16 00:00','2005-03-15 00:00','2005-02-18 00:00','2004-02-18 00:00','2003-10-27 00:00','2003-10-22 00:00','2003-10-02 00:00','2003-09-15 00:00','2003-02-20 00:00','2003-12-18 00:00','2002-09-30 00:00','2002-07-24 00:00','2002-04-26 00:00','2001-08-22 00:00'))
_DataIfMIBObjects_ObjectIdentity=ObjectIdentity
dataIfMIBObjects=_DataIfMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,15,35,1))
class _DataIfT38BasePort_Type(Unsigned32):defaultValue=6004;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1025,64535))
_DataIfT38BasePort_Type.__name__=_E
_DataIfT38BasePort_Object=MibScalar
dataIfT38BasePort=_DataIfT38BasePort_Object((1,3,6,1,4,1,4935,15,35,1,15),_DataIfT38BasePort_Type())
dataIfT38BasePort.setMaxAccess(_C)
if mibBuilder.loadTexts:dataIfT38BasePort.setStatus(_A)
_DataIfTable_Object=MibTable
dataIfTable=_DataIfTable_Object((1,3,6,1,4,1,4935,15,35,1,18))
if mibBuilder.loadTexts:dataIfTable.setStatus(_A)
_DataIfEntry_Object=MibTableRow
dataIfEntry=_DataIfEntry_Object((1,3,6,1,4,1,4935,15,35,1,18,50))
dataIfEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:dataIfEntry.setStatus(_A)
class _DataIfCngToneDetectionEnable_Type(MxEnableState):defaultValue=1
_DataIfCngToneDetectionEnable_Type.__name__=_F
_DataIfCngToneDetectionEnable_Object=MibTableColumn
dataIfCngToneDetectionEnable=_DataIfCngToneDetectionEnable_Object((1,3,6,1,4,1,4935,15,35,1,18,50,50),_DataIfCngToneDetectionEnable_Type())
dataIfCngToneDetectionEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:dataIfCngToneDetectionEnable.setStatus(_A)
class _DataIfCedFaxToneEnable_Type(MxEnableState):defaultValue=0
_DataIfCedFaxToneEnable_Type.__name__=_F
_DataIfCedFaxToneEnable_Object=MibTableColumn
dataIfCedFaxToneEnable=_DataIfCedFaxToneEnable_Object((1,3,6,1,4,1,4935,15,35,1,18,50,100),_DataIfCedFaxToneEnable_Type())
dataIfCedFaxToneEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:dataIfCedFaxToneEnable.setStatus(_A)
class _DataIfAnalogCedDetectionBehavior_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('passthrough',100),('faxmode',200)))
_DataIfAnalogCedDetectionBehavior_Type.__name__=_D
_DataIfAnalogCedDetectionBehavior_Object=MibTableColumn
dataIfAnalogCedDetectionBehavior=_DataIfAnalogCedDetectionBehavior_Object((1,3,6,1,4,1,4935,15,35,1,18,50,150),_DataIfAnalogCedDetectionBehavior_Type())
dataIfAnalogCedDetectionBehavior.setMaxAccess(_C)
if mibBuilder.loadTexts:dataIfAnalogCedDetectionBehavior.setStatus(_A)
_DataIfCodecTable_Object=MibTable
dataIfCodecTable=_DataIfCodecTable_Object((1,3,6,1,4,1,4935,15,35,1,20))
if mibBuilder.loadTexts:dataIfCodecTable.setStatus(_A)
_DataIfCodecEntry_Object=MibTableRow
dataIfCodecEntry=_DataIfCodecEntry_Object((1,3,6,1,4,1,4935,15,35,1,20,1))
dataIfCodecEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:dataIfCodecEntry.setStatus(_A)
class _DataIfCodecMediaTypeImageEnable_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_I,0),('pcmu',1),('pcma',2),('pcmu-pcma',3),('g726',4),('pcmu-g726',5),('pcma-g726',6),('pcmu-pcma-g726',7)))
_DataIfCodecMediaTypeImageEnable_Type.__name__=_D
_DataIfCodecMediaTypeImageEnable_Object=MibTableColumn
dataIfCodecMediaTypeImageEnable=_DataIfCodecMediaTypeImageEnable_Object((1,3,6,1,4,1,4935,15,35,1,20,1,1),_DataIfCodecMediaTypeImageEnable_Type())
dataIfCodecMediaTypeImageEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:dataIfCodecMediaTypeImageEnable.setStatus(_A)
class _DataIfClearChannelCodecPreferred_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,5,6,7)));namedValues=NamedValues(*(('pcmu',1),('pcma',2),('g726-32kbs',5),('g726-40kbs',6),('noPreferredCodec',7)))
_DataIfClearChannelCodecPreferred_Type.__name__=_D
_DataIfClearChannelCodecPreferred_Object=MibTableColumn
dataIfClearChannelCodecPreferred=_DataIfClearChannelCodecPreferred_Object((1,3,6,1,4,1,4935,15,35,1,20,1,2),_DataIfClearChannelCodecPreferred_Type())
dataIfClearChannelCodecPreferred.setMaxAccess(_C)
if mibBuilder.loadTexts:dataIfClearChannelCodecPreferred.setStatus(_A)
class _DataIfCodecT38Enable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_I,0),('enable',1),('signalingProtocolDependent',2)))
_DataIfCodecT38Enable_Type.__name__=_D
_DataIfCodecT38Enable_Object=MibTableColumn
dataIfCodecT38Enable=_DataIfCodecT38Enable_Object((1,3,6,1,4,1,4935,15,35,1,20,1,5),_DataIfCodecT38Enable_Type())
dataIfCodecT38Enable.setMaxAccess(_C)
if mibBuilder.loadTexts:dataIfCodecT38Enable.setStatus(_A)
class _DataIfCodecT38ProtectionLevel_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_DataIfCodecT38ProtectionLevel_Type.__name__=_E
_DataIfCodecT38ProtectionLevel_Object=MibTableColumn
dataIfCodecT38ProtectionLevel=_DataIfCodecT38ProtectionLevel_Object((1,3,6,1,4,1,4935,15,35,1,20,1,6),_DataIfCodecT38ProtectionLevel_Type())
dataIfCodecT38ProtectionLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:dataIfCodecT38ProtectionLevel.setStatus(_A)
class _DataIfT38FinalFramesRedundancy_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_DataIfT38FinalFramesRedundancy_Type.__name__=_E
_DataIfT38FinalFramesRedundancy_Object=MibScalar
dataIfT38FinalFramesRedundancy=_DataIfT38FinalFramesRedundancy_Object((1,3,6,1,4,1,4935,15,35,1,40),_DataIfT38FinalFramesRedundancy_Type())
dataIfT38FinalFramesRedundancy.setMaxAccess(_C)
if mibBuilder.loadTexts:dataIfT38FinalFramesRedundancy.setStatus(_A)
class _DataIfT38NoSignalEnable_Type(MxEnableState):defaultValue=0
_DataIfT38NoSignalEnable_Type.__name__=_F
_DataIfT38NoSignalEnable_Object=MibScalar
dataIfT38NoSignalEnable=_DataIfT38NoSignalEnable_Object((1,3,6,1,4,1,4935,15,35,1,90),_DataIfT38NoSignalEnable_Type())
dataIfT38NoSignalEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:dataIfT38NoSignalEnable.setStatus(_A)
class _DataIfT38NoSignalTimeout_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_DataIfT38NoSignalTimeout_Type.__name__=_E
_DataIfT38NoSignalTimeout_Object=MibScalar
dataIfT38NoSignalTimeout=_DataIfT38NoSignalTimeout_Object((1,3,6,1,4,1,4935,15,35,1,140),_DataIfT38NoSignalTimeout_Type())
dataIfT38NoSignalTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:dataIfT38NoSignalTimeout.setStatus(_A)
_DataIfConformance_ObjectIdentity=ObjectIdentity
dataIfConformance=_DataIfConformance_ObjectIdentity((1,3,6,1,4,1,4935,15,35,2))
_DataIfCompliances_ObjectIdentity=ObjectIdentity
dataIfCompliances=_DataIfCompliances_ObjectIdentity((1,3,6,1,4,1,4935,15,35,2,1))
_DataIfGroups_ObjectIdentity=ObjectIdentity
dataIfGroups=_DataIfGroups_ObjectIdentity((1,3,6,1,4,1,4935,15,35,2,2))
dataIfGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,15,35,2,2,1))
dataIfGroupVer1.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:dataIfGroupVer1.setStatus(_A)
dataIfComplVer1=ModuleCompliance((1,3,6,1,4,1,4935,15,35,2,1,1))
dataIfComplVer1.setObjects((_B,_U))
if mibBuilder.loadTexts:dataIfComplVer1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'dataIfMIB':dataIfMIB,'dataIfMIBObjects':dataIfMIBObjects,_T:dataIfT38BasePort,'dataIfTable':dataIfTable,'dataIfEntry':dataIfEntry,_J:dataIfCngToneDetectionEnable,_K:dataIfCedFaxToneEnable,_L:dataIfAnalogCedDetectionBehavior,'dataIfCodecTable':dataIfCodecTable,'dataIfCodecEntry':dataIfCodecEntry,_N:dataIfCodecMediaTypeImageEnable,_O:dataIfClearChannelCodecPreferred,_M:dataIfCodecT38Enable,_P:dataIfCodecT38ProtectionLevel,_Q:dataIfT38FinalFramesRedundancy,_R:dataIfT38NoSignalEnable,_S:dataIfT38NoSignalTimeout,'dataIfConformance':dataIfConformance,'dataIfCompliances':dataIfCompliances,'dataIfComplVer1':dataIfComplVer1,'dataIfGroups':dataIfGroups,_U:dataIfGroupVer1})