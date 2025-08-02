_J='hpnsaHSDevIndex'
_I='hpnsaHSDevModuleIndex'
_H='hpnsaHSModuleIndex'
_G='hpnsaHSAgentIndex'
_F='OctetString'
_E='DisplayString'
_D='HPNSAHOTSWAPSUBSYSTEM-MIB'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
_Hp_ObjectIdentity=ObjectIdentity
hp=_Hp_ObjectIdentity((1,3,6,1,4,1,11))
_Nm_ObjectIdentity=ObjectIdentity
nm=_Nm_ObjectIdentity((1,3,6,1,4,1,11,2))
_Hpnsa_ObjectIdentity=ObjectIdentity
hpnsa=_Hpnsa_ObjectIdentity((1,3,6,1,4,1,11,2,23))
_HpnsaHotSwap_ObjectIdentity=ObjectIdentity
hpnsaHotSwap=_HpnsaHotSwap_ObjectIdentity((1,3,6,1,4,1,11,2,23,20))
_HpnsaHSMibRev_ObjectIdentity=ObjectIdentity
hpnsaHSMibRev=_HpnsaHSMibRev_ObjectIdentity((1,3,6,1,4,1,11,2,23,20,1))
class _HpnsaHSMibRevMajor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnsaHSMibRevMajor_Type.__name__=_C
_HpnsaHSMibRevMajor_Object=MibScalar
hpnsaHSMibRevMajor=_HpnsaHSMibRevMajor_Object((1,3,6,1,4,1,11,2,23,20,1,1),_HpnsaHSMibRevMajor_Type())
hpnsaHSMibRevMajor.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaHSMibRevMajor.setStatus(_A)
class _HpnsaHSMibRevMinor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnsaHSMibRevMinor_Type.__name__=_C
_HpnsaHSMibRevMinor_Object=MibScalar
hpnsaHSMibRevMinor=_HpnsaHSMibRevMinor_Object((1,3,6,1,4,1,11,2,23,20,1,2),_HpnsaHSMibRevMinor_Type())
hpnsaHSMibRevMinor.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaHSMibRevMinor.setStatus(_A)
_HpnsaHSAgent_ObjectIdentity=ObjectIdentity
hpnsaHSAgent=_HpnsaHSAgent_ObjectIdentity((1,3,6,1,4,1,11,2,23,20,2))
_HpnsaHSAgentTable_Object=MibTable
hpnsaHSAgentTable=_HpnsaHSAgentTable_Object((1,3,6,1,4,1,11,2,23,20,2,1))
if mibBuilder.loadTexts:hpnsaHSAgentTable.setStatus(_A)
_HpnsaHSAgentEntry_Object=MibTableRow
hpnsaHSAgentEntry=_HpnsaHSAgentEntry_Object((1,3,6,1,4,1,11,2,23,20,2,1,1))
hpnsaHSAgentEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:hpnsaHSAgentEntry.setStatus(_A)
class _HpnsaHSAgentIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnsaHSAgentIndex_Type.__name__=_C
_HpnsaHSAgentIndex_Object=MibTableColumn
hpnsaHSAgentIndex=_HpnsaHSAgentIndex_Object((1,3,6,1,4,1,11,2,23,20,2,1,1,1),_HpnsaHSAgentIndex_Type())
hpnsaHSAgentIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaHSAgentIndex.setStatus(_A)
class _HpnsaHSAgentName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnsaHSAgentName_Type.__name__=_E
_HpnsaHSAgentName_Object=MibTableColumn
hpnsaHSAgentName=_HpnsaHSAgentName_Object((1,3,6,1,4,1,11,2,23,20,2,1,1,2),_HpnsaHSAgentName_Type())
hpnsaHSAgentName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaHSAgentName.setStatus(_A)
class _HpnsaHSAgentVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_HpnsaHSAgentVersion_Type.__name__=_E
_HpnsaHSAgentVersion_Object=MibTableColumn
hpnsaHSAgentVersion=_HpnsaHSAgentVersion_Object((1,3,6,1,4,1,11,2,23,20,2,1,1,3),_HpnsaHSAgentVersion_Type())
hpnsaHSAgentVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaHSAgentVersion.setStatus(_A)
class _HpnsaHSAgentDate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_HpnsaHSAgentDate_Type.__name__=_F
_HpnsaHSAgentDate_Object=MibTableColumn
hpnsaHSAgentDate=_HpnsaHSAgentDate_Object((1,3,6,1,4,1,11,2,23,20,2,1,1,4),_HpnsaHSAgentDate_Type())
hpnsaHSAgentDate.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaHSAgentDate.setStatus(_A)
_HpnsaHSModule_ObjectIdentity=ObjectIdentity
hpnsaHSModule=_HpnsaHSModule_ObjectIdentity((1,3,6,1,4,1,11,2,23,20,3))
_HpnsaHSModuleTable_Object=MibTable
hpnsaHSModuleTable=_HpnsaHSModuleTable_Object((1,3,6,1,4,1,11,2,23,20,3,1))
if mibBuilder.loadTexts:hpnsaHSModuleTable.setStatus(_A)
_HpnsaHSModuleEntry_Object=MibTableRow
hpnsaHSModuleEntry=_HpnsaHSModuleEntry_Object((1,3,6,1,4,1,11,2,23,20,3,1,1))
hpnsaHSModuleEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:hpnsaHSModuleEntry.setStatus(_A)
_HpnsaHSModuleIndex_Type=Integer32
_HpnsaHSModuleIndex_Object=MibTableColumn
hpnsaHSModuleIndex=_HpnsaHSModuleIndex_Object((1,3,6,1,4,1,11,2,23,20,3,1,1,1),_HpnsaHSModuleIndex_Type())
hpnsaHSModuleIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaHSModuleIndex.setStatus(_A)
class _HpnsaHSModuleScsiCableType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('wide',1),('narrow',2),('error',3),('no-cable',4)))
_HpnsaHSModuleScsiCableType_Type.__name__=_C
_HpnsaHSModuleScsiCableType_Object=MibTableColumn
hpnsaHSModuleScsiCableType=_HpnsaHSModuleScsiCableType_Object((1,3,6,1,4,1,11,2,23,20,3,1,1,2),_HpnsaHSModuleScsiCableType_Type())
hpnsaHSModuleScsiCableType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaHSModuleScsiCableType.setStatus(_A)
class _HpnsaHSModuleTempStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('error',1),('normal',2),('warning',3),('emergency',4)))
_HpnsaHSModuleTempStatus_Type.__name__=_C
_HpnsaHSModuleTempStatus_Object=MibTableColumn
hpnsaHSModuleTempStatus=_HpnsaHSModuleTempStatus_Object((1,3,6,1,4,1,11,2,23,20,3,1,1,3),_HpnsaHSModuleTempStatus_Type())
hpnsaHSModuleTempStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaHSModuleTempStatus.setStatus(_A)
class _HpnsaHSModuleSwitchState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disabled',1),('enabled',2)))
_HpnsaHSModuleSwitchState_Type.__name__=_C
_HpnsaHSModuleSwitchState_Object=MibTableColumn
hpnsaHSModuleSwitchState=_HpnsaHSModuleSwitchState_Object((1,3,6,1,4,1,11,2,23,20,3,1,1,4),_HpnsaHSModuleSwitchState_Type())
hpnsaHSModuleSwitchState.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaHSModuleSwitchState.setStatus(_A)
class _HpnsaHSModuleDeviceStartup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('at-poweron',1),('by-start-command',2)))
_HpnsaHSModuleDeviceStartup_Type.__name__=_C
_HpnsaHSModuleDeviceStartup_Object=MibTableColumn
hpnsaHSModuleDeviceStartup=_HpnsaHSModuleDeviceStartup_Object((1,3,6,1,4,1,11,2,23,20,3,1,1,5),_HpnsaHSModuleDeviceStartup_Type())
hpnsaHSModuleDeviceStartup.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaHSModuleDeviceStartup.setStatus(_A)
class _HpnsaHSModuleMiddleDrvAddr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('lowest',1),('default',2)))
_HpnsaHSModuleMiddleDrvAddr_Type.__name__=_C
_HpnsaHSModuleMiddleDrvAddr_Object=MibTableColumn
hpnsaHSModuleMiddleDrvAddr=_HpnsaHSModuleMiddleDrvAddr_Object((1,3,6,1,4,1,11,2,23,20,3,1,1,6),_HpnsaHSModuleMiddleDrvAddr_Type())
hpnsaHSModuleMiddleDrvAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaHSModuleMiddleDrvAddr.setStatus(_A)
class _HpnsaHSModuleHi8ScsiAddr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('hi-range-9to15',1),('lo-range-1to7',2)))
_HpnsaHSModuleHi8ScsiAddr_Type.__name__=_C
_HpnsaHSModuleHi8ScsiAddr_Object=MibTableColumn
hpnsaHSModuleHi8ScsiAddr=_HpnsaHSModuleHi8ScsiAddr_Object((1,3,6,1,4,1,11,2,23,20,3,1,1,7),_HpnsaHSModuleHi8ScsiAddr_Type())
hpnsaHSModuleHi8ScsiAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaHSModuleHi8ScsiAddr.setStatus(_A)
_HpnsaHSDev_ObjectIdentity=ObjectIdentity
hpnsaHSDev=_HpnsaHSDev_ObjectIdentity((1,3,6,1,4,1,11,2,23,20,4))
_HpnsaHSDevTable_Object=MibTable
hpnsaHSDevTable=_HpnsaHSDevTable_Object((1,3,6,1,4,1,11,2,23,20,4,1))
if mibBuilder.loadTexts:hpnsaHSDevTable.setStatus(_A)
_HpnsaHSDevEntry_Object=MibTableRow
hpnsaHSDevEntry=_HpnsaHSDevEntry_Object((1,3,6,1,4,1,11,2,23,20,4,1,1))
hpnsaHSDevEntry.setIndexNames((0,_D,_I),(0,_D,_J))
if mibBuilder.loadTexts:hpnsaHSDevEntry.setStatus(_A)
class _HpnsaHSDevModuleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnsaHSDevModuleIndex_Type.__name__=_C
_HpnsaHSDevModuleIndex_Object=MibTableColumn
hpnsaHSDevModuleIndex=_HpnsaHSDevModuleIndex_Object((1,3,6,1,4,1,11,2,23,20,4,1,1,1),_HpnsaHSDevModuleIndex_Type())
hpnsaHSDevModuleIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaHSDevModuleIndex.setStatus(_A)
_HpnsaHSDevIndex_Type=Integer32
_HpnsaHSDevIndex_Object=MibTableColumn
hpnsaHSDevIndex=_HpnsaHSDevIndex_Object((1,3,6,1,4,1,11,2,23,20,4,1,1,2),_HpnsaHSDevIndex_Type())
hpnsaHSDevIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaHSDevIndex.setStatus(_A)
class _HpnsaHSDevExistence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('present',1),('not-present',2)))
_HpnsaHSDevExistence_Type.__name__=_C
_HpnsaHSDevExistence_Object=MibTableColumn
hpnsaHSDevExistence=_HpnsaHSDevExistence_Object((1,3,6,1,4,1,11,2,23,20,4,1,1,3),_HpnsaHSDevExistence_Type())
hpnsaHSDevExistence.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaHSDevExistence.setStatus(_A)
_HpnsaHSDevScsiAddr_Type=Integer32
_HpnsaHSDevScsiAddr_Object=MibTableColumn
hpnsaHSDevScsiAddr=_HpnsaHSDevScsiAddr_Object((1,3,6,1,4,1,11,2,23,20,4,1,1,4),_HpnsaHSDevScsiAddr_Type())
hpnsaHSDevScsiAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaHSDevScsiAddr.setStatus(_A)
class _HpnsaHSDevPowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('not-connected',1),('connected',2)))
_HpnsaHSDevPowerStatus_Type.__name__=_C
_HpnsaHSDevPowerStatus_Object=MibTableColumn
hpnsaHSDevPowerStatus=_HpnsaHSDevPowerStatus_Object((1,3,6,1,4,1,11,2,23,20,4,1,1,5),_HpnsaHSDevPowerStatus_Type())
hpnsaHSDevPowerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaHSDevPowerStatus.setStatus(_A)
class _HpnsaHSPwrAlertDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnsaHSPwrAlertDelay_Type.__name__=_C
_HpnsaHSPwrAlertDelay_Object=MibScalar
hpnsaHSPwrAlertDelay=_HpnsaHSPwrAlertDelay_Object((1,3,6,1,4,1,11,2,23,20,4,2),_HpnsaHSPwrAlertDelay_Type())
hpnsaHSPwrAlertDelay.setMaxAccess('read-write')
if mibBuilder.loadTexts:hpnsaHSPwrAlertDelay.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'hp':hp,'nm':nm,'hpnsa':hpnsa,'hpnsaHotSwap':hpnsaHotSwap,'hpnsaHSMibRev':hpnsaHSMibRev,'hpnsaHSMibRevMajor':hpnsaHSMibRevMajor,'hpnsaHSMibRevMinor':hpnsaHSMibRevMinor,'hpnsaHSAgent':hpnsaHSAgent,'hpnsaHSAgentTable':hpnsaHSAgentTable,'hpnsaHSAgentEntry':hpnsaHSAgentEntry,_G:hpnsaHSAgentIndex,'hpnsaHSAgentName':hpnsaHSAgentName,'hpnsaHSAgentVersion':hpnsaHSAgentVersion,'hpnsaHSAgentDate':hpnsaHSAgentDate,'hpnsaHSModule':hpnsaHSModule,'hpnsaHSModuleTable':hpnsaHSModuleTable,'hpnsaHSModuleEntry':hpnsaHSModuleEntry,_H:hpnsaHSModuleIndex,'hpnsaHSModuleScsiCableType':hpnsaHSModuleScsiCableType,'hpnsaHSModuleTempStatus':hpnsaHSModuleTempStatus,'hpnsaHSModuleSwitchState':hpnsaHSModuleSwitchState,'hpnsaHSModuleDeviceStartup':hpnsaHSModuleDeviceStartup,'hpnsaHSModuleMiddleDrvAddr':hpnsaHSModuleMiddleDrvAddr,'hpnsaHSModuleHi8ScsiAddr':hpnsaHSModuleHi8ScsiAddr,'hpnsaHSDev':hpnsaHSDev,'hpnsaHSDevTable':hpnsaHSDevTable,'hpnsaHSDevEntry':hpnsaHSDevEntry,_I:hpnsaHSDevModuleIndex,_J:hpnsaHSDevIndex,'hpnsaHSDevExistence':hpnsaHSDevExistence,'hpnsaHSDevScsiAddr':hpnsaHSDevScsiAddr,'hpnsaHSDevPowerStatus':hpnsaHSDevPowerStatus,'hpnsaHSPwrAlertDelay':hpnsaHSPwrAlertDelay})