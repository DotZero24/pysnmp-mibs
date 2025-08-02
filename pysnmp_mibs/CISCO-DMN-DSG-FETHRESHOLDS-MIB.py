_E='mutingThreshholdsInstance'
_D='CISCO-DMN-DSG-FETHRESHOLDS-MIB'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoDSGUtilities,=mibBuilder.importSymbols('CISCO-DMN-DSG-ROOT-MIB','ciscoDSGUtilities')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoDSGFeThresholds=ModuleIdentity((1,3,6,1,4,1,1429,2,2,5,9))
if mibBuilder.loadTexts:ciscoDSGFeThresholds.setRevisions(('2010-08-30 11:00','2010-04-26 05:00','2010-03-22 05:00','2009-12-07 12:00'))
_MutingThresholdsTable_Object=MibTable
mutingThresholdsTable=_MutingThresholdsTable_Object((1,3,6,1,4,1,1429,2,2,5,9,1))
if mibBuilder.loadTexts:mutingThresholdsTable.setStatus(_A)
_MutingThresholdsEntry_Object=MibTableRow
mutingThresholdsEntry=_MutingThresholdsEntry_Object((1,3,6,1,4,1,1429,2,2,5,9,1,1))
mutingThresholdsEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:mutingThresholdsEntry.setStatus(_A)
class _MutingThreshholdsInstance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_MutingThreshholdsInstance_Type.__name__=_B
_MutingThreshholdsInstance_Object=MibTableColumn
mutingThreshholdsInstance=_MutingThreshholdsInstance_Object((1,3,6,1,4,1,1429,2,2,5,9,1,1,1),_MutingThreshholdsInstance_Type())
mutingThreshholdsInstance.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:mutingThreshholdsInstance.setStatus(_A)
class _MutThreshRestoreDefaults_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('writeOnly',1),('yes',2)))
_MutThreshRestoreDefaults_Type.__name__=_B
_MutThreshRestoreDefaults_Object=MibTableColumn
mutThreshRestoreDefaults=_MutThreshRestoreDefaults_Object((1,3,6,1,4,1,1429,2,2,5,9,1,1,2),_MutThreshRestoreDefaults_Type())
mutThreshRestoreDefaults.setMaxAccess(_C)
if mibBuilder.loadTexts:mutThreshRestoreDefaults.setStatus(_A)
class _MutThreshControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disable',1),('enable',2)))
_MutThreshControl_Type.__name__=_B
_MutThreshControl_Object=MibTableColumn
mutThreshControl=_MutThreshControl_Object((1,3,6,1,4,1,1429,2,2,5,9,1,1,3),_MutThreshControl_Type())
mutThreshControl.setMaxAccess(_C)
if mibBuilder.loadTexts:mutThreshControl.setStatus(_A)
class _MutThreshDVBSTransportMute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-50,200))
_MutThreshDVBSTransportMute_Type.__name__=_B
_MutThreshDVBSTransportMute_Object=MibTableColumn
mutThreshDVBSTransportMute=_MutThreshDVBSTransportMute_Object((1,3,6,1,4,1,1429,2,2,5,9,1,1,4),_MutThreshDVBSTransportMute_Type())
mutThreshDVBSTransportMute.setMaxAccess(_C)
if mibBuilder.loadTexts:mutThreshDVBSTransportMute.setStatus(_A)
class _MutThreshDVBSTransportRestore_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-50,200))
_MutThreshDVBSTransportRestore_Type.__name__=_B
_MutThreshDVBSTransportRestore_Object=MibTableColumn
mutThreshDVBSTransportRestore=_MutThreshDVBSTransportRestore_Object((1,3,6,1,4,1,1429,2,2,5,9,1,1,5),_MutThreshDVBSTransportRestore_Type())
mutThreshDVBSTransportRestore.setMaxAccess(_C)
if mibBuilder.loadTexts:mutThreshDVBSTransportRestore.setStatus(_A)
class _MutThreshDVBSAudioMute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-50,200))
_MutThreshDVBSAudioMute_Type.__name__=_B
_MutThreshDVBSAudioMute_Object=MibTableColumn
mutThreshDVBSAudioMute=_MutThreshDVBSAudioMute_Object((1,3,6,1,4,1,1429,2,2,5,9,1,1,6),_MutThreshDVBSAudioMute_Type())
mutThreshDVBSAudioMute.setMaxAccess(_C)
if mibBuilder.loadTexts:mutThreshDVBSAudioMute.setStatus(_A)
class _MutThreshDVBSAudioRestore_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-50,200))
_MutThreshDVBSAudioRestore_Type.__name__=_B
_MutThreshDVBSAudioRestore_Object=MibTableColumn
mutThreshDVBSAudioRestore=_MutThreshDVBSAudioRestore_Object((1,3,6,1,4,1,1429,2,2,5,9,1,1,7),_MutThreshDVBSAudioRestore_Type())
mutThreshDVBSAudioRestore.setMaxAccess(_C)
if mibBuilder.loadTexts:mutThreshDVBSAudioRestore.setStatus(_A)
class _MutThreshDVBS2TransportMute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-50,200))
_MutThreshDVBS2TransportMute_Type.__name__=_B
_MutThreshDVBS2TransportMute_Object=MibTableColumn
mutThreshDVBS2TransportMute=_MutThreshDVBS2TransportMute_Object((1,3,6,1,4,1,1429,2,2,5,9,1,1,8),_MutThreshDVBS2TransportMute_Type())
mutThreshDVBS2TransportMute.setMaxAccess(_C)
if mibBuilder.loadTexts:mutThreshDVBS2TransportMute.setStatus(_A)
class _MutThreshDVBS2TransportRestore_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-50,200))
_MutThreshDVBS2TransportRestore_Type.__name__=_B
_MutThreshDVBS2TransportRestore_Object=MibTableColumn
mutThreshDVBS2TransportRestore=_MutThreshDVBS2TransportRestore_Object((1,3,6,1,4,1,1429,2,2,5,9,1,1,9),_MutThreshDVBS2TransportRestore_Type())
mutThreshDVBS2TransportRestore.setMaxAccess(_C)
if mibBuilder.loadTexts:mutThreshDVBS2TransportRestore.setStatus(_A)
class _MutThreshDVBS2AudioMute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-50,200))
_MutThreshDVBS2AudioMute_Type.__name__=_B
_MutThreshDVBS2AudioMute_Object=MibTableColumn
mutThreshDVBS2AudioMute=_MutThreshDVBS2AudioMute_Object((1,3,6,1,4,1,1429,2,2,5,9,1,1,10),_MutThreshDVBS2AudioMute_Type())
mutThreshDVBS2AudioMute.setMaxAccess(_C)
if mibBuilder.loadTexts:mutThreshDVBS2AudioMute.setStatus(_A)
class _MutThreshDVBS2AudioRestore_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-50,200))
_MutThreshDVBS2AudioRestore_Type.__name__=_B
_MutThreshDVBS2AudioRestore_Object=MibTableColumn
mutThreshDVBS2AudioRestore=_MutThreshDVBS2AudioRestore_Object((1,3,6,1,4,1,1429,2,2,5,9,1,1,11),_MutThreshDVBS2AudioRestore_Type())
mutThreshDVBS2AudioRestore.setMaxAccess(_C)
if mibBuilder.loadTexts:mutThreshDVBS2AudioRestore.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'ciscoDSGFeThresholds':ciscoDSGFeThresholds,'mutingThresholdsTable':mutingThresholdsTable,'mutingThresholdsEntry':mutingThresholdsEntry,_E:mutingThreshholdsInstance,'mutThreshRestoreDefaults':mutThreshRestoreDefaults,'mutThreshControl':mutThreshControl,'mutThreshDVBSTransportMute':mutThreshDVBSTransportMute,'mutThreshDVBSTransportRestore':mutThreshDVBSTransportRestore,'mutThreshDVBSAudioMute':mutThreshDVBSAudioMute,'mutThreshDVBSAudioRestore':mutThreshDVBSAudioRestore,'mutThreshDVBS2TransportMute':mutThreshDVBS2TransportMute,'mutThreshDVBS2TransportRestore':mutThreshDVBS2TransportRestore,'mutThreshDVBS2AudioMute':mutThreshDVBS2AudioMute,'mutThreshDVBS2AudioRestore':mutThreshDVBS2AudioRestore})