_M='rcmcPortSD'
_L='rcmcPortFefi'
_K='rcmcPortFaultReturnStatus'
_J='rcmcPortFaultPassStatus'
_I='EnableVar'
_H='unavailable'
_G='normal'
_F='read-write'
_E='read-only'
_D='rcmcPortIndex'
_C='Integer32'
_B='CONVERTOR-SYSTEM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
iscomMediaConvertor,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','iscomMediaConvertor')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
EnableVar,PortList=mibBuilder.importSymbols('SWITCH-TC',_I,'PortList')
rcmcSystem=ModuleIdentity((1,3,6,1,4,1,8886,16,1,1))
_RcmcOamConfig_ObjectIdentity=ObjectIdentity
rcmcOamConfig=_RcmcOamConfig_ObjectIdentity((1,3,6,1,4,1,8886,16,1,1,1))
_RcmcOamEnable_Type=EnableVar
_RcmcOamEnable_Object=MibScalar
rcmcOamEnable=_RcmcOamEnable_Object((1,3,6,1,4,1,8886,16,1,1,1,1),_RcmcOamEnable_Type())
rcmcOamEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:rcmcOamEnable.setStatus(_A)
class _RcmcOamWorkMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('masterCtrl',1),('slaveCtrl',2)))
_RcmcOamWorkMode_Type.__name__=_C
_RcmcOamWorkMode_Object=MibScalar
rcmcOamWorkMode=_RcmcOamWorkMode_Object((1,3,6,1,4,1,8886,16,1,1,1,2),_RcmcOamWorkMode_Type())
rcmcOamWorkMode.setMaxAccess(_F)
if mibBuilder.loadTexts:rcmcOamWorkMode.setStatus(_A)
_RcmcOamConfigTrap_ObjectIdentity=ObjectIdentity
rcmcOamConfigTrap=_RcmcOamConfigTrap_ObjectIdentity((1,3,6,1,4,1,8886,16,1,1,1,3))
_RcmcPortInfoConfig_ObjectIdentity=ObjectIdentity
rcmcPortInfoConfig=_RcmcPortInfoConfig_ObjectIdentity((1,3,6,1,4,1,8886,16,1,1,2))
_RcmcPortTable_Object=MibTable
rcmcPortTable=_RcmcPortTable_Object((1,3,6,1,4,1,8886,16,1,1,2,1))
if mibBuilder.loadTexts:rcmcPortTable.setStatus(_A)
_RcmcPortEntry_Object=MibTableRow
rcmcPortEntry=_RcmcPortEntry_Object((1,3,6,1,4,1,8886,16,1,1,2,1,1))
rcmcPortEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:rcmcPortEntry.setStatus(_A)
_RcmcPortIndex_Type=Integer32
_RcmcPortIndex_Object=MibTableColumn
rcmcPortIndex=_RcmcPortIndex_Object((1,3,6,1,4,1,8886,16,1,1,2,1,1,1),_RcmcPortIndex_Type())
rcmcPortIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:rcmcPortIndex.setStatus(_A)
class _RcmcPortOptModuleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('optical-M',1),('optical-S1',2),('optical-S2',3),('optical-S3',4),('optical-SS13',5),('optical-SS15',6),('optical-SS23',7),('optical-SS25',8),('optical-SS35',9),('unknown',10)))
_RcmcPortOptModuleType_Type.__name__=_C
_RcmcPortOptModuleType_Object=MibTableColumn
rcmcPortOptModuleType=_RcmcPortOptModuleType_Object((1,3,6,1,4,1,8886,16,1,1,2,1,1,2),_RcmcPortOptModuleType_Type())
rcmcPortOptModuleType.setMaxAccess(_E)
if mibBuilder.loadTexts:rcmcPortOptModuleType.setStatus(_A)
class _RcmcPortFaultPassEnable_Type(EnableVar):defaultValue=2
_RcmcPortFaultPassEnable_Type.__name__=_I
_RcmcPortFaultPassEnable_Object=MibTableColumn
rcmcPortFaultPassEnable=_RcmcPortFaultPassEnable_Object((1,3,6,1,4,1,8886,16,1,1,2,1,1,3),_RcmcPortFaultPassEnable_Type())
rcmcPortFaultPassEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:rcmcPortFaultPassEnable.setStatus(_A)
class _RcmcPortFaultPassStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),('down',2)))
_RcmcPortFaultPassStatus_Type.__name__=_C
_RcmcPortFaultPassStatus_Object=MibTableColumn
rcmcPortFaultPassStatus=_RcmcPortFaultPassStatus_Object((1,3,6,1,4,1,8886,16,1,1,2,1,1,4),_RcmcPortFaultPassStatus_Type())
rcmcPortFaultPassStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:rcmcPortFaultPassStatus.setStatus(_A)
class _RcmcPortSD_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),('sd',2),(_H,3)))
_RcmcPortSD_Type.__name__=_C
_RcmcPortSD_Object=MibTableColumn
rcmcPortSD=_RcmcPortSD_Object((1,3,6,1,4,1,8886,16,1,1,2,1,1,5),_RcmcPortSD_Type())
rcmcPortSD.setMaxAccess(_E)
if mibBuilder.loadTexts:rcmcPortSD.setStatus(_A)
class _RcmcPortFaultReturnEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('enable',1),('disable',2),(_H,3)))
_RcmcPortFaultReturnEnable_Type.__name__=_C
_RcmcPortFaultReturnEnable_Object=MibTableColumn
rcmcPortFaultReturnEnable=_RcmcPortFaultReturnEnable_Object((1,3,6,1,4,1,8886,16,1,1,2,1,1,6),_RcmcPortFaultReturnEnable_Type())
rcmcPortFaultReturnEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:rcmcPortFaultReturnEnable.setStatus(_A)
class _RcmcPortFaultReturnStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),('down',2),(_H,3)))
_RcmcPortFaultReturnStatus_Type.__name__=_C
_RcmcPortFaultReturnStatus_Object=MibTableColumn
rcmcPortFaultReturnStatus=_RcmcPortFaultReturnStatus_Object((1,3,6,1,4,1,8886,16,1,1,2,1,1,7),_RcmcPortFaultReturnStatus_Type())
rcmcPortFaultReturnStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:rcmcPortFaultReturnStatus.setStatus(_A)
class _RcmcPortFefi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),('fefi',2),(_H,3)))
_RcmcPortFefi_Type.__name__=_C
_RcmcPortFefi_Object=MibTableColumn
rcmcPortFefi=_RcmcPortFefi_Object((1,3,6,1,4,1,8886,16,1,1,2,1,1,8),_RcmcPortFefi_Type())
rcmcPortFefi.setMaxAccess(_E)
if mibBuilder.loadTexts:rcmcPortFefi.setStatus(_A)
_RcmcPortFPToPorts_Type=PortList
_RcmcPortFPToPorts_Object=MibTableColumn
rcmcPortFPToPorts=_RcmcPortFPToPorts_Object((1,3,6,1,4,1,8886,16,1,1,2,1,1,9),_RcmcPortFPToPorts_Type())
rcmcPortFPToPorts.setMaxAccess(_F)
if mibBuilder.loadTexts:rcmcPortFPToPorts.setStatus(_A)
_RcmcPortInfoTrap_ObjectIdentity=ObjectIdentity
rcmcPortInfoTrap=_RcmcPortInfoTrap_ObjectIdentity((1,3,6,1,4,1,8886,16,1,1,2,2))
rcmcOamRemoteLostTrap=NotificationType((1,3,6,1,4,1,8886,16,1,1,1,3,1))
if mibBuilder.loadTexts:rcmcOamRemoteLostTrap.setStatus(_A)
rcmcOamRemoteRecoverTrap=NotificationType((1,3,6,1,4,1,8886,16,1,1,1,3,2))
if mibBuilder.loadTexts:rcmcOamRemoteRecoverTrap.setStatus(_A)
rcmcPortFaultPassTrap=NotificationType((1,3,6,1,4,1,8886,16,1,1,2,2,1))
rcmcPortFaultPassTrap.setObjects(*((_B,_D),(_B,_J)))
if mibBuilder.loadTexts:rcmcPortFaultPassTrap.setStatus(_A)
rcmcPortFaultReturnTrap=NotificationType((1,3,6,1,4,1,8886,16,1,1,2,2,2))
rcmcPortFaultReturnTrap.setObjects(*((_B,_D),(_B,_K)))
if mibBuilder.loadTexts:rcmcPortFaultReturnTrap.setStatus(_A)
rcmcPortFefiTrap=NotificationType((1,3,6,1,4,1,8886,16,1,1,2,2,3))
rcmcPortFefiTrap.setObjects(*((_B,_D),(_B,_L)))
if mibBuilder.loadTexts:rcmcPortFefiTrap.setStatus(_A)
rcmcPortSDTrap=NotificationType((1,3,6,1,4,1,8886,16,1,1,2,2,4))
rcmcPortSDTrap.setObjects(*((_B,_D),(_B,_M)))
if mibBuilder.loadTexts:rcmcPortSDTrap.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'rcmcSystem':rcmcSystem,'rcmcOamConfig':rcmcOamConfig,'rcmcOamEnable':rcmcOamEnable,'rcmcOamWorkMode':rcmcOamWorkMode,'rcmcOamConfigTrap':rcmcOamConfigTrap,'rcmcOamRemoteLostTrap':rcmcOamRemoteLostTrap,'rcmcOamRemoteRecoverTrap':rcmcOamRemoteRecoverTrap,'rcmcPortInfoConfig':rcmcPortInfoConfig,'rcmcPortTable':rcmcPortTable,'rcmcPortEntry':rcmcPortEntry,_D:rcmcPortIndex,'rcmcPortOptModuleType':rcmcPortOptModuleType,'rcmcPortFaultPassEnable':rcmcPortFaultPassEnable,_J:rcmcPortFaultPassStatus,_M:rcmcPortSD,'rcmcPortFaultReturnEnable':rcmcPortFaultReturnEnable,_K:rcmcPortFaultReturnStatus,_L:rcmcPortFefi,'rcmcPortFPToPorts':rcmcPortFPToPorts,'rcmcPortInfoTrap':rcmcPortInfoTrap,'rcmcPortFaultPassTrap':rcmcPortFaultPassTrap,'rcmcPortFaultReturnTrap':rcmcPortFaultReturnTrap,'rcmcPortFefiTrap':rcmcPortFefiTrap,'rcmcPortSDTrap':rcmcPortSDTrap})