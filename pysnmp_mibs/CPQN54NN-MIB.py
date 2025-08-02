_I='secondary'
_H='primary'
_G='read-only'
_F='NotificationType'
_E='mandatory'
_D='Integer32'
_C='sysUpTime'
_B='sysDescr'
_A='SNMPv2-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysDescr,sysUpTime=mibBuilder.importSymbols(_A,_B,_C)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier',_F,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_F,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Compaq_ObjectIdentity=ObjectIdentity
compaq=_Compaq_ObjectIdentity((1,3,6,1,4,1,232))
_CpqGigaSwitch_ObjectIdentity=ObjectIdentity
cpqGigaSwitch=_CpqGigaSwitch_ObjectIdentity((1,3,6,1,4,1,232,111))
_CpqGigaSwitchProd_ObjectIdentity=ObjectIdentity
cpqGigaSwitchProd=_CpqGigaSwitchProd_ObjectIdentity((1,3,6,1,4,1,232,111,1))
_CpqGigaSwitchId5422_ObjectIdentity=ObjectIdentity
cpqGigaSwitchId5422=_CpqGigaSwitchId5422_ObjectIdentity((1,3,6,1,4,1,232,111,1,1))
_CpqGigaSwitchId5411_ObjectIdentity=ObjectIdentity
cpqGigaSwitchId5411=_CpqGigaSwitchId5411_ObjectIdentity((1,3,6,1,4,1,232,111,1,2))
_CpqOids_ObjectIdentity=ObjectIdentity
cpqOids=_CpqOids_ObjectIdentity((1,3,6,1,4,1,232,111,2))
_CpqMauType_ObjectIdentity=ObjectIdentity
cpqMauType=_CpqMauType_ObjectIdentity((1,3,6,1,4,1,232,111,2,1))
_CpqMauType1000BaseSX_ObjectIdentity=ObjectIdentity
cpqMauType1000BaseSX=_CpqMauType1000BaseSX_ObjectIdentity((1,3,6,1,4,1,232,111,2,1,1))
_CpqMauType1000BaseLX_ObjectIdentity=ObjectIdentity
cpqMauType1000BaseLX=_CpqMauType1000BaseLX_ObjectIdentity((1,3,6,1,4,1,232,111,2,1,2))
_CpqMauType1000BaseCX_ObjectIdentity=ObjectIdentity
cpqMauType1000BaseCX=_CpqMauType1000BaseCX_ObjectIdentity((1,3,6,1,4,1,232,111,2,1,3))
_CpqMauType1000BaseSXFD_ObjectIdentity=ObjectIdentity
cpqMauType1000BaseSXFD=_CpqMauType1000BaseSXFD_ObjectIdentity((1,3,6,1,4,1,232,111,2,1,4))
_CpqMauType1000BaseLXFD_ObjectIdentity=ObjectIdentity
cpqMauType1000BaseLXFD=_CpqMauType1000BaseLXFD_ObjectIdentity((1,3,6,1,4,1,232,111,2,1,5))
_CpqMauType1000BaseCXFD_ObjectIdentity=ObjectIdentity
cpqMauType1000BaseCXFD=_CpqMauType1000BaseCXFD_ObjectIdentity((1,3,6,1,4,1,232,111,2,1,6))
_CpqGigaSwitchMib_ObjectIdentity=ObjectIdentity
cpqGigaSwitchMib=_CpqGigaSwitchMib_ObjectIdentity((1,3,6,1,4,1,232,111,3))
_CpqGigaSwitchSystem_ObjectIdentity=ObjectIdentity
cpqGigaSwitchSystem=_CpqGigaSwitchSystem_ObjectIdentity((1,3,6,1,4,1,232,111,3,1))
class _CpqSaveConfiguration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('saveToPrimary',1),('saveToSecondary',2)))
_CpqSaveConfiguration_Type.__name__=_D
_CpqSaveConfiguration_Object=MibScalar
cpqSaveConfiguration=_CpqSaveConfiguration_Object((1,3,6,1,4,1,232,111,3,1,3),_CpqSaveConfiguration_Type())
cpqSaveConfiguration.setMaxAccess('write-only')
if mibBuilder.loadTexts:cpqSaveConfiguration.setStatus(_E)
class _CpqSaveStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('saveInProgress',1),('saveNotInProgress',2)))
_CpqSaveStatus_Type.__name__=_D
_CpqSaveStatus_Object=MibScalar
cpqSaveStatus=_CpqSaveStatus_Object((1,3,6,1,4,1,232,111,3,1,4),_CpqSaveStatus_Type())
cpqSaveStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:cpqSaveStatus.setStatus(_E)
class _CpqCurrentConfigInUse_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_CpqCurrentConfigInUse_Type.__name__=_D
_CpqCurrentConfigInUse_Object=MibScalar
cpqCurrentConfigInUse=_CpqCurrentConfigInUse_Object((1,3,6,1,4,1,232,111,3,1,5),_CpqCurrentConfigInUse_Type())
cpqCurrentConfigInUse.setMaxAccess(_G)
if mibBuilder.loadTexts:cpqCurrentConfigInUse.setStatus(_E)
class _CpqConfigToUseOnReboot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_CpqConfigToUseOnReboot_Type.__name__=_D
_CpqConfigToUseOnReboot_Object=MibScalar
cpqConfigToUseOnReboot=_CpqConfigToUseOnReboot_Object((1,3,6,1,4,1,232,111,3,1,6),_CpqConfigToUseOnReboot_Type())
cpqConfigToUseOnReboot.setMaxAccess('read-write')
if mibBuilder.loadTexts:cpqConfigToUseOnReboot.setStatus(_E)
overheat=NotificationType((1,3,6,1,4,1,232,111,0,6))
overheat.setObjects(*((_A,_C),(_A,_B)))
if mibBuilder.loadTexts:overheat.setStatus('')
fanfailed=NotificationType((1,3,6,1,4,1,232,111,0,7))
fanfailed.setObjects(*((_A,_C),(_A,_B)))
if mibBuilder.loadTexts:fanfailed.setStatus('')
fanOK=NotificationType((1,3,6,1,4,1,232,111,0,8))
fanOK.setObjects(*((_A,_C),(_A,_B)))
if mibBuilder.loadTexts:fanOK.setStatus('')
invalidLoginAttempt=NotificationType((1,3,6,1,4,1,232,111,0,9))
invalidLoginAttempt.setObjects(*((_A,_C),(_A,_B)))
if mibBuilder.loadTexts:invalidLoginAttempt.setStatus('')
powerSupplyFail=NotificationType((1,3,6,1,4,1,232,111,0,10))
powerSupplyFail.setObjects(*((_A,_C),(_A,_B)))
if mibBuilder.loadTexts:powerSupplyFail.setStatus('')
powerSupplyGood=NotificationType((1,3,6,1,4,1,232,111,0,11))
powerSupplyGood.setObjects(*((_A,_C),(_A,_B)))
if mibBuilder.loadTexts:powerSupplyGood.setStatus('')
rpsAlarm=NotificationType((1,3,6,1,4,1,232,111,0,12))
rpsAlarm.setObjects(*((_A,_C),(_A,_B)))
if mibBuilder.loadTexts:rpsAlarm.setStatus('')
rpsNoAlarm=NotificationType((1,3,6,1,4,1,232,111,0,13))
rpsNoAlarm.setObjects(*((_A,_C),(_A,_B)))
if mibBuilder.loadTexts:rpsNoAlarm.setStatus('')
mibBuilder.exportSymbols('CPQN54NN-MIB',**{'compaq':compaq,'cpqGigaSwitch':cpqGigaSwitch,'overheat':overheat,'fanfailed':fanfailed,'fanOK':fanOK,'invalidLoginAttempt':invalidLoginAttempt,'powerSupplyFail':powerSupplyFail,'powerSupplyGood':powerSupplyGood,'rpsAlarm':rpsAlarm,'rpsNoAlarm':rpsNoAlarm,'cpqGigaSwitchProd':cpqGigaSwitchProd,'cpqGigaSwitchId5422':cpqGigaSwitchId5422,'cpqGigaSwitchId5411':cpqGigaSwitchId5411,'cpqOids':cpqOids,'cpqMauType':cpqMauType,'cpqMauType1000BaseSX':cpqMauType1000BaseSX,'cpqMauType1000BaseLX':cpqMauType1000BaseLX,'cpqMauType1000BaseCX':cpqMauType1000BaseCX,'cpqMauType1000BaseSXFD':cpqMauType1000BaseSXFD,'cpqMauType1000BaseLXFD':cpqMauType1000BaseLXFD,'cpqMauType1000BaseCXFD':cpqMauType1000BaseCXFD,'cpqGigaSwitchMib':cpqGigaSwitchMib,'cpqGigaSwitchSystem':cpqGigaSwitchSystem,'cpqSaveConfiguration':cpqSaveConfiguration,'cpqSaveStatus':cpqSaveStatus,'cpqCurrentConfigInUse':cpqCurrentConfigInUse,'cpqConfigToUseOnReboot':cpqConfigToUseOnReboot})