_k='cpqSasSwitchHwRedundancyState'
_j='cpqSasSwitchHwStatus'
_i='failed'
_h='NotificationType'
_g='CPQSASSWITCH-MIB'
_f='degraded'
_e='other'
_d='cpqSsBoxVendor'
_c='cpqSsBoxSerialNumber'
_b='cpqSsBoxModel'
_a='cpqSsBoxLocationString'
_Z='cpqSsBoxCondition'
_Y='cpqSsBoxCntlrIndex'
_X='cpqSsBoxCntlrHwLocation'
_W='cpqSsBoxBusIndex'
_V='cpqDaPhyDrvType'
_U='cpqDaPhyDrvSerialNum'
_T='cpqDaPhyDrvModel'
_S='cpqDaPhyDrvLocationString'
_R='cpqDaPhyDrvIndex'
_Q='cpqDaPhyDrvFWRev'
_P='cpqDaPhyDrvCntlrIndex'
_O='cpqDaPhyDrvBoxOnConnector'
_N='cpqSiSysSerialNum'
_M='cpqSiSysProductId'
_L='cpqSiProductName'
_K='mandatory'
_J='read-only'
_I='cpqHoTrapFlags'
_H='CPQHOST-MIB'
_G='Integer32'
_F='sysLocation'
_E='sysName'
_D='CPQSINFO-MIB'
_C='SNMPv2-MIB'
_B='CPQSTSYS-MIB'
_A='CPQIDA-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
compaq,cpqHoTrapFlags=mibBuilder.importSymbols(_H,'compaq',_I)
cpqDaPhyDrvBoxOnConnector,cpqDaPhyDrvCntlrIndex,cpqDaPhyDrvFWRev,cpqDaPhyDrvIndex,cpqDaPhyDrvLocationString,cpqDaPhyDrvModel,cpqDaPhyDrvSerialNum,cpqDaPhyDrvStatus,cpqDaPhyDrvType=mibBuilder.importSymbols(_A,_O,_P,_Q,_R,_S,_T,_U,'cpqDaPhyDrvStatus',_V)
cpqSiProductName,cpqSiSysProductId,cpqSiSysSerialNum=mibBuilder.importSymbols(_D,_L,_M,_N)
cpqSsBoxBusIndex,cpqSsBoxCntlrHwLocation,cpqSsBoxCntlrIndex,cpqSsBoxCondition,cpqSsBoxLocationString,cpqSsBoxModel,cpqSsBoxSerialNumber,cpqSsBoxVendor=mibBuilder.importSymbols(_B,_W,_X,_Y,_Z,_a,_b,_c,_d)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysLocation,sysName=mibBuilder.importSymbols(_C,_F,_E)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier',_h,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_h,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_CpqSasSwitch_ObjectIdentity=ObjectIdentity
cpqSasSwitch=_CpqSasSwitch_ObjectIdentity((1,3,6,1,4,1,232,25))
_CpqSasSwitchMibRev_ObjectIdentity=ObjectIdentity
cpqSasSwitchMibRev=_CpqSasSwitchMibRev_ObjectIdentity((1,3,6,1,4,1,232,25,1))
class _CpqSasSwitchMibRevMajor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CpqSasSwitchMibRevMajor_Type.__name__=_G
_CpqSasSwitchMibRevMajor_Object=MibScalar
cpqSasSwitchMibRevMajor=_CpqSasSwitchMibRevMajor_Object((1,3,6,1,4,1,232,25,1,1),_CpqSasSwitchMibRevMajor_Type())
cpqSasSwitchMibRevMajor.setMaxAccess(_J)
if mibBuilder.loadTexts:cpqSasSwitchMibRevMajor.setStatus(_K)
class _CpqSasSwitchMibRevMinor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSasSwitchMibRevMinor_Type.__name__=_G
_CpqSasSwitchMibRevMinor_Object=MibScalar
cpqSasSwitchMibRevMinor=_CpqSasSwitchMibRevMinor_Object((1,3,6,1,4,1,232,25,1,2),_CpqSasSwitchMibRevMinor_Type())
cpqSasSwitchMibRevMinor.setMaxAccess(_J)
if mibBuilder.loadTexts:cpqSasSwitchMibRevMinor.setStatus(_K)
class _CpqSasSwitchMibCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_e,1),('ok',2),(_f,3),(_i,4)))
_CpqSasSwitchMibCondition_Type.__name__=_G
_CpqSasSwitchMibCondition_Object=MibScalar
cpqSasSwitchMibCondition=_CpqSasSwitchMibCondition_Object((1,3,6,1,4,1,232,25,1,3),_CpqSasSwitchMibCondition_Type())
cpqSasSwitchMibCondition.setMaxAccess(_J)
if mibBuilder.loadTexts:cpqSasSwitchMibCondition.setStatus(_K)
_CpqSasSwitchComponent_ObjectIdentity=ObjectIdentity
cpqSasSwitchComponent=_CpqSasSwitchComponent_ObjectIdentity((1,3,6,1,4,1,232,25,2))
_CpqSasSwitchInterface_ObjectIdentity=ObjectIdentity
cpqSasSwitchInterface=_CpqSasSwitchInterface_ObjectIdentity((1,3,6,1,4,1,232,25,2,1))
_CpqSasSwitchOsCommon_ObjectIdentity=ObjectIdentity
cpqSasSwitchOsCommon=_CpqSasSwitchOsCommon_ObjectIdentity((1,3,6,1,4,1,232,25,2,1,4))
_CpqSasSwitchHw_ObjectIdentity=ObjectIdentity
cpqSasSwitchHw=_CpqSasSwitchHw_ObjectIdentity((1,3,6,1,4,1,232,25,2,2))
_CpqSasSwitchHwType_ObjectIdentity=ObjectIdentity
cpqSasSwitchHwType=_CpqSasSwitchHwType_ObjectIdentity((1,3,6,1,4,1,232,25,2,2,1))
class _CpqSasSwitchHwStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_e,1),('ok',2),(_f,3),(_i,4)))
_CpqSasSwitchHwStatus_Type.__name__=_G
_CpqSasSwitchHwStatus_Object=MibScalar
cpqSasSwitchHwStatus=_CpqSasSwitchHwStatus_Object((1,3,6,1,4,1,232,25,2,2,2),_CpqSasSwitchHwStatus_Type())
cpqSasSwitchHwStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:cpqSasSwitchHwStatus.setStatus(_K)
class _CpqSasSwitchHwRedundancyState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_e,1),('active',2),('standby',3),('notConfigured',4),('notRedundant',5),(_f,6),('mismatch',7)))
_CpqSasSwitchHwRedundancyState_Type.__name__=_G
_CpqSasSwitchHwRedundancyState_Object=MibScalar
cpqSasSwitchHwRedundancyState=_CpqSasSwitchHwRedundancyState_Object((1,3,6,1,4,1,232,25,2,2,3),_CpqSasSwitchHwRedundancyState_Type())
cpqSasSwitchHwRedundancyState.setMaxAccess(_J)
if mibBuilder.loadTexts:cpqSasSwitchHwRedundancyState.setStatus(_K)
cpqSasSwitchTestTrap=NotificationType((1,3,6,1,4,1,232,25,0,1))
cpqSasSwitchTestTrap.setObjects(*((_D,_L),(_D,_M),(_D,_N),(_C,_E),(_C,_F)))
if mibBuilder.loadTexts:cpqSasSwitchTestTrap.setStatus('')
cpqSasSwitchHwStatusChangeTrap=NotificationType((1,3,6,1,4,1,232,25,0,101))
cpqSasSwitchHwStatusChangeTrap.setObjects(*((_D,_L),(_D,_M),(_D,_N),(_C,_E),(_C,_F),(_g,_j)))
if mibBuilder.loadTexts:cpqSasSwitchHwStatusChangeTrap.setStatus('')
cpqSasSwitchHwRedundancyStateChangeTrap=NotificationType((1,3,6,1,4,1,232,25,0,201))
cpqSasSwitchHwRedundancyStateChangeTrap.setObjects(*((_D,_L),(_D,_M),(_D,_N),(_C,_E),(_C,_F),(_g,_k)))
if mibBuilder.loadTexts:cpqSasSwitchHwRedundancyStateChangeTrap.setStatus('')
cpqSasSwitchPhysicalDriveAddedTrap=NotificationType((1,3,6,1,4,1,232,25,0,301))
cpqSasSwitchPhysicalDriveAddedTrap.setObjects(*((_C,_E),(_H,_I),(_C,_F),(_A,_P),(_A,_R),(_A,_S),(_A,_V),(_A,_T),(_A,_Q),(_A,_U),(_A,_O)))
if mibBuilder.loadTexts:cpqSasSwitchPhysicalDriveAddedTrap.setStatus('')
cpqSasSwitchPhysicalDriveRemovedTrap=NotificationType((1,3,6,1,4,1,232,25,0,302))
cpqSasSwitchPhysicalDriveRemovedTrap.setObjects(*((_C,_E),(_H,_I),(_C,_F),(_A,_P),(_A,_R),(_A,_S),(_A,_V),(_A,_T),(_A,_Q),(_A,_U),(_A,_O)))
if mibBuilder.loadTexts:cpqSasSwitchPhysicalDriveRemovedTrap.setStatus('')
cpqSasSwitchStorageEnclosureAddedTrap=NotificationType((1,3,6,1,4,1,232,25,0,401))
cpqSasSwitchStorageEnclosureAddedTrap.setObjects(*((_C,_E),(_H,_I),(_B,_X),(_B,_Y),(_B,_W),(_B,_d),(_B,_b),(_B,_c),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:cpqSasSwitchStorageEnclosureAddedTrap.setStatus('')
cpqSasSwitchStorageEnclosureRemovedTrap=NotificationType((1,3,6,1,4,1,232,25,0,402))
cpqSasSwitchStorageEnclosureRemovedTrap.setObjects(*((_C,_E),(_H,_I),(_B,_X),(_B,_Y),(_B,_W),(_B,_d),(_B,_b),(_B,_c),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:cpqSasSwitchStorageEnclosureRemovedTrap.setStatus('')
mibBuilder.exportSymbols(_g,**{'cpqSasSwitch':cpqSasSwitch,'cpqSasSwitchTestTrap':cpqSasSwitchTestTrap,'cpqSasSwitchHwStatusChangeTrap':cpqSasSwitchHwStatusChangeTrap,'cpqSasSwitchHwRedundancyStateChangeTrap':cpqSasSwitchHwRedundancyStateChangeTrap,'cpqSasSwitchPhysicalDriveAddedTrap':cpqSasSwitchPhysicalDriveAddedTrap,'cpqSasSwitchPhysicalDriveRemovedTrap':cpqSasSwitchPhysicalDriveRemovedTrap,'cpqSasSwitchStorageEnclosureAddedTrap':cpqSasSwitchStorageEnclosureAddedTrap,'cpqSasSwitchStorageEnclosureRemovedTrap':cpqSasSwitchStorageEnclosureRemovedTrap,'cpqSasSwitchMibRev':cpqSasSwitchMibRev,'cpqSasSwitchMibRevMajor':cpqSasSwitchMibRevMajor,'cpqSasSwitchMibRevMinor':cpqSasSwitchMibRevMinor,'cpqSasSwitchMibCondition':cpqSasSwitchMibCondition,'cpqSasSwitchComponent':cpqSasSwitchComponent,'cpqSasSwitchInterface':cpqSasSwitchInterface,'cpqSasSwitchOsCommon':cpqSasSwitchOsCommon,'cpqSasSwitchHw':cpqSasSwitchHw,'cpqSasSwitchHwType':cpqSasSwitchHwType,_j:cpqSasSwitchHwStatus,_k:cpqSasSwitchHwRedundancyState})