_l='coIfXcvrLSCMIBGroup'
_k='coIfXcvrTunableLaserMIBGroup'
_j='coIfXcvrBaseMIBGroup'
_i='coIfXcvrLSCPulseRepetitionTime'
_h='coIfXcvrLSCTestPulseLength'
_g='coIfXcvrLSCPulseLength'
_f='coIfXcvrLSCManualRestart'
_e='coIfXcvrLSCRestartMode'
_d='coIfXcvrLSCProtocol'
_c='coIfXcvrLaserSafetyControl'
_b='coIfXcvrLaserFrequencyBitmap'
_a='coIfXcvrLaserFrequencySpacing'
_Z='coIfXcvrMinLaserFrequency'
_Y='coIfXcvrForwardLaserControl'
_X='coIfXcvrLaserOperStatus'
_W='coIfXcvrLaserAdminStatus'
_V='coIfDwdmChannelGroupBitmap'
_U='coIfDwdmChannelGroupBitmapLogic'
_T='coIfDwdmChannelGroupSpacing'
_S='coIfDwdmChannelGroupMinFrequency'
_R='coIfDwdmFrequency'
_Q='coIfTypeExtn'
_P='seconds'
_O='disable'
_N='enable'
_M='coIfDwdmChannelGroupMIBGroup'
_L='coIfTypeExtnMIBGroup'
_K='coIfWavelengthMIBGroup'
_J='read-only'
_I='OctetString'
_H='GHz'
_G='ifIndex'
_F='IF-MIB'
_E='Unsigned32'
_D='Integer32'
_C='read-write'
_B='CISCO-OPTICAL-IF-EXTN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
ifIndex,=mibBuilder.importSymbols(_F,_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoOpticalIfExtnMIB=ModuleIdentity((1,3,6,1,4,1,9,10,66))
if mibBuilder.loadTexts:ciscoOpticalIfExtnMIB.setRevisions(('2004-11-19 00:00','2003-12-29 00:00','2002-05-23 00:00','2001-04-20 00:00'))
class CoDwdmFrequency(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000000))
class CoDwdmFrequencyOrZero(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_CoIfExtnMIBObjects_ObjectIdentity=ObjectIdentity
coIfExtnMIBObjects=_CoIfExtnMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,10,66,1))
_CoIfTypeExtnGroup_ObjectIdentity=ObjectIdentity
coIfTypeExtnGroup=_CoIfTypeExtnGroup_ObjectIdentity((1,3,6,1,4,1,9,10,66,1,1))
_CoIfTypeExtnTable_Object=MibTable
coIfTypeExtnTable=_CoIfTypeExtnTable_Object((1,3,6,1,4,1,9,10,66,1,1,1))
if mibBuilder.loadTexts:coIfTypeExtnTable.setStatus(_A)
_CoIfTypeExtnEntry_Object=MibTableRow
coIfTypeExtnEntry=_CoIfTypeExtnEntry_Object((1,3,6,1,4,1,9,10,66,1,1,1,1))
coIfTypeExtnEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:coIfTypeExtnEntry.setStatus(_A)
class _CoIfTypeExtn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('opticalTransponder',1),('wdmTransport',2),('wdmChannel',3),('wdmChannelGroup',4),('wavelengthTransport',5),('ethernetPhy',6),('esconPhy',7),('gigabitPhy',8),('twoGigabitPhy',9),('sonetPhy',10),('multiRate',11)))
_CoIfTypeExtn_Type.__name__=_D
_CoIfTypeExtn_Object=MibTableColumn
coIfTypeExtn=_CoIfTypeExtn_Object((1,3,6,1,4,1,9,10,66,1,1,1,1,1),_CoIfTypeExtn_Type())
coIfTypeExtn.setMaxAccess(_J)
if mibBuilder.loadTexts:coIfTypeExtn.setStatus(_A)
_CoIfWavelengthGroup_ObjectIdentity=ObjectIdentity
coIfWavelengthGroup=_CoIfWavelengthGroup_ObjectIdentity((1,3,6,1,4,1,9,10,66,1,2))
_CoIfWavelengthTable_Object=MibTable
coIfWavelengthTable=_CoIfWavelengthTable_Object((1,3,6,1,4,1,9,10,66,1,2,1))
if mibBuilder.loadTexts:coIfWavelengthTable.setStatus(_A)
_CoIfWavelengthEntry_Object=MibTableRow
coIfWavelengthEntry=_CoIfWavelengthEntry_Object((1,3,6,1,4,1,9,10,66,1,2,1,1))
coIfWavelengthEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:coIfWavelengthEntry.setStatus(_A)
_CoIfDwdmFrequency_Type=CoDwdmFrequency
_CoIfDwdmFrequency_Object=MibTableColumn
coIfDwdmFrequency=_CoIfDwdmFrequency_Object((1,3,6,1,4,1,9,10,66,1,2,1,1,1),_CoIfDwdmFrequency_Type())
coIfDwdmFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:coIfDwdmFrequency.setStatus(_A)
if mibBuilder.loadTexts:coIfDwdmFrequency.setUnits(_H)
_CoIfDwdmChannelGroup_ObjectIdentity=ObjectIdentity
coIfDwdmChannelGroup=_CoIfDwdmChannelGroup_ObjectIdentity((1,3,6,1,4,1,9,10,66,1,3))
_CoIfDwdmChannelGroupTable_Object=MibTable
coIfDwdmChannelGroupTable=_CoIfDwdmChannelGroupTable_Object((1,3,6,1,4,1,9,10,66,1,3,3))
if mibBuilder.loadTexts:coIfDwdmChannelGroupTable.setStatus(_A)
_CoIfDwdmChannelGroupEntry_Object=MibTableRow
coIfDwdmChannelGroupEntry=_CoIfDwdmChannelGroupEntry_Object((1,3,6,1,4,1,9,10,66,1,3,3,1))
coIfDwdmChannelGroupEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:coIfDwdmChannelGroupEntry.setStatus(_A)
_CoIfDwdmChannelGroupMinFrequency_Type=CoDwdmFrequency
_CoIfDwdmChannelGroupMinFrequency_Object=MibTableColumn
coIfDwdmChannelGroupMinFrequency=_CoIfDwdmChannelGroupMinFrequency_Object((1,3,6,1,4,1,9,10,66,1,3,3,1,1),_CoIfDwdmChannelGroupMinFrequency_Type())
coIfDwdmChannelGroupMinFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:coIfDwdmChannelGroupMinFrequency.setStatus(_A)
if mibBuilder.loadTexts:coIfDwdmChannelGroupMinFrequency.setUnits(_H)
class _CoIfDwdmChannelGroupSpacing_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_CoIfDwdmChannelGroupSpacing_Type.__name__=_E
_CoIfDwdmChannelGroupSpacing_Object=MibTableColumn
coIfDwdmChannelGroupSpacing=_CoIfDwdmChannelGroupSpacing_Object((1,3,6,1,4,1,9,10,66,1,3,3,1,2),_CoIfDwdmChannelGroupSpacing_Type())
coIfDwdmChannelGroupSpacing.setMaxAccess(_C)
if mibBuilder.loadTexts:coIfDwdmChannelGroupSpacing.setStatus(_A)
if mibBuilder.loadTexts:coIfDwdmChannelGroupSpacing.setUnits(_H)
class _CoIfDwdmChannelGroupBitmapLogic_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('carried',1),('blocked',2)))
_CoIfDwdmChannelGroupBitmapLogic_Type.__name__=_D
_CoIfDwdmChannelGroupBitmapLogic_Object=MibTableColumn
coIfDwdmChannelGroupBitmapLogic=_CoIfDwdmChannelGroupBitmapLogic_Object((1,3,6,1,4,1,9,10,66,1,3,3,1,3),_CoIfDwdmChannelGroupBitmapLogic_Type())
coIfDwdmChannelGroupBitmapLogic.setMaxAccess(_C)
if mibBuilder.loadTexts:coIfDwdmChannelGroupBitmapLogic.setStatus(_A)
class _CoIfDwdmChannelGroupBitmap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CoIfDwdmChannelGroupBitmap_Type.__name__=_I
_CoIfDwdmChannelGroupBitmap_Object=MibTableColumn
coIfDwdmChannelGroupBitmap=_CoIfDwdmChannelGroupBitmap_Object((1,3,6,1,4,1,9,10,66,1,3,3,1,4),_CoIfDwdmChannelGroupBitmap_Type())
coIfDwdmChannelGroupBitmap.setMaxAccess(_C)
if mibBuilder.loadTexts:coIfDwdmChannelGroupBitmap.setStatus(_A)
_CoIfXcvrGroup_ObjectIdentity=ObjectIdentity
coIfXcvrGroup=_CoIfXcvrGroup_ObjectIdentity((1,3,6,1,4,1,9,10,66,1,4))
_CoIfXcvrTable_Object=MibTable
coIfXcvrTable=_CoIfXcvrTable_Object((1,3,6,1,4,1,9,10,66,1,4,1))
if mibBuilder.loadTexts:coIfXcvrTable.setStatus(_A)
_CoIfXcvrEntry_Object=MibTableRow
coIfXcvrEntry=_CoIfXcvrEntry_Object((1,3,6,1,4,1,9,10,66,1,4,1,1))
coIfXcvrEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:coIfXcvrEntry.setStatus(_A)
class _CoIfXcvrLaserAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_CoIfXcvrLaserAdminStatus_Type.__name__=_D
_CoIfXcvrLaserAdminStatus_Object=MibTableColumn
coIfXcvrLaserAdminStatus=_CoIfXcvrLaserAdminStatus_Object((1,3,6,1,4,1,9,10,66,1,4,1,1,1),_CoIfXcvrLaserAdminStatus_Type())
coIfXcvrLaserAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:coIfXcvrLaserAdminStatus.setStatus(_A)
class _CoIfXcvrLaserOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('transmitting',1),('degraded',2),('down',3),('lscDown',4),('flcDown',5),('unknown',6)))
_CoIfXcvrLaserOperStatus_Type.__name__=_D
_CoIfXcvrLaserOperStatus_Object=MibTableColumn
coIfXcvrLaserOperStatus=_CoIfXcvrLaserOperStatus_Object((1,3,6,1,4,1,9,10,66,1,4,1,1,2),_CoIfXcvrLaserOperStatus_Type())
coIfXcvrLaserOperStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:coIfXcvrLaserOperStatus.setStatus(_A)
_CoIfXcvrMinLaserFrequency_Type=CoDwdmFrequencyOrZero
_CoIfXcvrMinLaserFrequency_Object=MibTableColumn
coIfXcvrMinLaserFrequency=_CoIfXcvrMinLaserFrequency_Object((1,3,6,1,4,1,9,10,66,1,4,1,1,3),_CoIfXcvrMinLaserFrequency_Type())
coIfXcvrMinLaserFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:coIfXcvrMinLaserFrequency.setStatus(_A)
if mibBuilder.loadTexts:coIfXcvrMinLaserFrequency.setUnits(_H)
class _CoIfXcvrLaserFrequencySpacing_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_CoIfXcvrLaserFrequencySpacing_Type.__name__=_E
_CoIfXcvrLaserFrequencySpacing_Object=MibTableColumn
coIfXcvrLaserFrequencySpacing=_CoIfXcvrLaserFrequencySpacing_Object((1,3,6,1,4,1,9,10,66,1,4,1,1,4),_CoIfXcvrLaserFrequencySpacing_Type())
coIfXcvrLaserFrequencySpacing.setMaxAccess(_C)
if mibBuilder.loadTexts:coIfXcvrLaserFrequencySpacing.setStatus(_A)
if mibBuilder.loadTexts:coIfXcvrLaserFrequencySpacing.setUnits(_H)
class _CoIfXcvrLaserFrequencyBitmap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CoIfXcvrLaserFrequencyBitmap_Type.__name__=_I
_CoIfXcvrLaserFrequencyBitmap_Object=MibTableColumn
coIfXcvrLaserFrequencyBitmap=_CoIfXcvrLaserFrequencyBitmap_Object((1,3,6,1,4,1,9,10,66,1,4,1,1,5),_CoIfXcvrLaserFrequencyBitmap_Type())
coIfXcvrLaserFrequencyBitmap.setMaxAccess(_J)
if mibBuilder.loadTexts:coIfXcvrLaserFrequencyBitmap.setStatus(_A)
class _CoIfXcvrForwardLaserControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_CoIfXcvrForwardLaserControl_Type.__name__=_D
_CoIfXcvrForwardLaserControl_Object=MibTableColumn
coIfXcvrForwardLaserControl=_CoIfXcvrForwardLaserControl_Object((1,3,6,1,4,1,9,10,66,1,4,1,1,6),_CoIfXcvrForwardLaserControl_Type())
coIfXcvrForwardLaserControl.setMaxAccess(_C)
if mibBuilder.loadTexts:coIfXcvrForwardLaserControl.setStatus(_A)
class _CoIfXcvrLaserSafetyControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_CoIfXcvrLaserSafetyControl_Type.__name__=_D
_CoIfXcvrLaserSafetyControl_Object=MibTableColumn
coIfXcvrLaserSafetyControl=_CoIfXcvrLaserSafetyControl_Object((1,3,6,1,4,1,9,10,66,1,4,1,1,7),_CoIfXcvrLaserSafetyControl_Type())
coIfXcvrLaserSafetyControl.setMaxAccess(_C)
if mibBuilder.loadTexts:coIfXcvrLaserSafetyControl.setStatus(_A)
class _CoIfXcvrLSCProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('proprietary',1),('g664',2)))
_CoIfXcvrLSCProtocol_Type.__name__=_D
_CoIfXcvrLSCProtocol_Object=MibTableColumn
coIfXcvrLSCProtocol=_CoIfXcvrLSCProtocol_Object((1,3,6,1,4,1,9,10,66,1,4,1,1,8),_CoIfXcvrLSCProtocol_Type())
coIfXcvrLSCProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:coIfXcvrLSCProtocol.setStatus(_A)
class _CoIfXcvrLSCRestartMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('automaticRestart',1),('manualRestart',2)))
_CoIfXcvrLSCRestartMode_Type.__name__=_D
_CoIfXcvrLSCRestartMode_Object=MibTableColumn
coIfXcvrLSCRestartMode=_CoIfXcvrLSCRestartMode_Object((1,3,6,1,4,1,9,10,66,1,4,1,1,9),_CoIfXcvrLSCRestartMode_Type())
coIfXcvrLSCRestartMode.setMaxAccess(_C)
if mibBuilder.loadTexts:coIfXcvrLSCRestartMode.setStatus(_A)
class _CoIfXcvrLSCManualRestart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noop',1),('restart',2),('restartForTest',3)))
_CoIfXcvrLSCManualRestart_Type.__name__=_D
_CoIfXcvrLSCManualRestart_Object=MibTableColumn
coIfXcvrLSCManualRestart=_CoIfXcvrLSCManualRestart_Object((1,3,6,1,4,1,9,10,66,1,4,1,1,10),_CoIfXcvrLSCManualRestart_Type())
coIfXcvrLSCManualRestart.setMaxAccess(_C)
if mibBuilder.loadTexts:coIfXcvrLSCManualRestart.setStatus(_A)
class _CoIfXcvrLSCPulseLength_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,20000))
_CoIfXcvrLSCPulseLength_Type.__name__=_E
_CoIfXcvrLSCPulseLength_Object=MibTableColumn
coIfXcvrLSCPulseLength=_CoIfXcvrLSCPulseLength_Object((1,3,6,1,4,1,9,10,66,1,4,1,1,11),_CoIfXcvrLSCPulseLength_Type())
coIfXcvrLSCPulseLength.setMaxAccess(_C)
if mibBuilder.loadTexts:coIfXcvrLSCPulseLength.setStatus(_A)
if mibBuilder.loadTexts:coIfXcvrLSCPulseLength.setUnits('milliseconds')
class _CoIfXcvrLSCTestPulseLength_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_CoIfXcvrLSCTestPulseLength_Type.__name__=_E
_CoIfXcvrLSCTestPulseLength_Object=MibTableColumn
coIfXcvrLSCTestPulseLength=_CoIfXcvrLSCTestPulseLength_Object((1,3,6,1,4,1,9,10,66,1,4,1,1,12),_CoIfXcvrLSCTestPulseLength_Type())
coIfXcvrLSCTestPulseLength.setMaxAccess(_C)
if mibBuilder.loadTexts:coIfXcvrLSCTestPulseLength.setStatus(_A)
if mibBuilder.loadTexts:coIfXcvrLSCTestPulseLength.setUnits(_P)
class _CoIfXcvrLSCPulseRepetitionTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_CoIfXcvrLSCPulseRepetitionTime_Type.__name__=_E
_CoIfXcvrLSCPulseRepetitionTime_Object=MibTableColumn
coIfXcvrLSCPulseRepetitionTime=_CoIfXcvrLSCPulseRepetitionTime_Object((1,3,6,1,4,1,9,10,66,1,4,1,1,13),_CoIfXcvrLSCPulseRepetitionTime_Type())
coIfXcvrLSCPulseRepetitionTime.setMaxAccess(_C)
if mibBuilder.loadTexts:coIfXcvrLSCPulseRepetitionTime.setStatus(_A)
if mibBuilder.loadTexts:coIfXcvrLSCPulseRepetitionTime.setUnits(_P)
_CoIfExtnMIBConformance_ObjectIdentity=ObjectIdentity
coIfExtnMIBConformance=_CoIfExtnMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,10,66,3))
_CoIfExtnMIBCompliances_ObjectIdentity=ObjectIdentity
coIfExtnMIBCompliances=_CoIfExtnMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,66,3,1))
_CoIfExtnMIBGroups_ObjectIdentity=ObjectIdentity
coIfExtnMIBGroups=_CoIfExtnMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,10,66,3,2))
coIfTypeExtnMIBGroup=ObjectGroup((1,3,6,1,4,1,9,10,66,3,2,1))
coIfTypeExtnMIBGroup.setObjects((_B,_Q))
if mibBuilder.loadTexts:coIfTypeExtnMIBGroup.setStatus(_A)
coIfWavelengthMIBGroup=ObjectGroup((1,3,6,1,4,1,9,10,66,3,2,2))
coIfWavelengthMIBGroup.setObjects((_B,_R))
if mibBuilder.loadTexts:coIfWavelengthMIBGroup.setStatus(_A)
coIfDwdmChannelGroupMIBGroup=ObjectGroup((1,3,6,1,4,1,9,10,66,3,2,3))
coIfDwdmChannelGroupMIBGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:coIfDwdmChannelGroupMIBGroup.setStatus(_A)
coIfXcvrBaseMIBGroup=ObjectGroup((1,3,6,1,4,1,9,10,66,3,2,4))
coIfXcvrBaseMIBGroup.setObjects(*((_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:coIfXcvrBaseMIBGroup.setStatus(_A)
coIfXcvrTunableLaserMIBGroup=ObjectGroup((1,3,6,1,4,1,9,10,66,3,2,5))
coIfXcvrTunableLaserMIBGroup.setObjects(*((_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:coIfXcvrTunableLaserMIBGroup.setStatus(_A)
coIfXcvrLSCMIBGroup=ObjectGroup((1,3,6,1,4,1,9,10,66,3,2,6))
coIfXcvrLSCMIBGroup.setObjects(*((_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i)))
if mibBuilder.loadTexts:coIfXcvrLSCMIBGroup.setStatus(_A)
coIfExtnMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,66,3,1,1))
coIfExtnMIBCompliance.setObjects(*((_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:coIfExtnMIBCompliance.setStatus('deprecated')
coIfExtnMIBCompliance2=ModuleCompliance((1,3,6,1,4,1,9,10,66,3,1,2))
coIfExtnMIBCompliance2.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_j),(_B,_k),(_B,_l)))
if mibBuilder.loadTexts:coIfExtnMIBCompliance2.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CoDwdmFrequency':CoDwdmFrequency,'CoDwdmFrequencyOrZero':CoDwdmFrequencyOrZero,'ciscoOpticalIfExtnMIB':ciscoOpticalIfExtnMIB,'coIfExtnMIBObjects':coIfExtnMIBObjects,'coIfTypeExtnGroup':coIfTypeExtnGroup,'coIfTypeExtnTable':coIfTypeExtnTable,'coIfTypeExtnEntry':coIfTypeExtnEntry,_Q:coIfTypeExtn,'coIfWavelengthGroup':coIfWavelengthGroup,'coIfWavelengthTable':coIfWavelengthTable,'coIfWavelengthEntry':coIfWavelengthEntry,_R:coIfDwdmFrequency,'coIfDwdmChannelGroup':coIfDwdmChannelGroup,'coIfDwdmChannelGroupTable':coIfDwdmChannelGroupTable,'coIfDwdmChannelGroupEntry':coIfDwdmChannelGroupEntry,_S:coIfDwdmChannelGroupMinFrequency,_T:coIfDwdmChannelGroupSpacing,_U:coIfDwdmChannelGroupBitmapLogic,_V:coIfDwdmChannelGroupBitmap,'coIfXcvrGroup':coIfXcvrGroup,'coIfXcvrTable':coIfXcvrTable,'coIfXcvrEntry':coIfXcvrEntry,_W:coIfXcvrLaserAdminStatus,_X:coIfXcvrLaserOperStatus,_Z:coIfXcvrMinLaserFrequency,_a:coIfXcvrLaserFrequencySpacing,_b:coIfXcvrLaserFrequencyBitmap,_Y:coIfXcvrForwardLaserControl,_c:coIfXcvrLaserSafetyControl,_d:coIfXcvrLSCProtocol,_e:coIfXcvrLSCRestartMode,_f:coIfXcvrLSCManualRestart,_g:coIfXcvrLSCPulseLength,_h:coIfXcvrLSCTestPulseLength,_i:coIfXcvrLSCPulseRepetitionTime,'coIfExtnMIBConformance':coIfExtnMIBConformance,'coIfExtnMIBCompliances':coIfExtnMIBCompliances,'coIfExtnMIBCompliance':coIfExtnMIBCompliance,'coIfExtnMIBCompliance2':coIfExtnMIBCompliance2,'coIfExtnMIBGroups':coIfExtnMIBGroups,_L:coIfTypeExtnMIBGroup,_K:coIfWavelengthMIBGroup,_M:coIfDwdmChannelGroupMIBGroup,_j:coIfXcvrBaseMIBGroup,_k:coIfXcvrTunableLaserMIBGroup,_l:coIfXcvrLSCMIBGroup})