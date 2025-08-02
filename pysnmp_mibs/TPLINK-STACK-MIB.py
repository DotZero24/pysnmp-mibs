_Q='unit-8'
_P='unit-7'
_O='unit-6'
_N='unit-5'
_M='unit-4'
_L='unit-3'
_K='unit-2'
_J='unit-1'
_I='tpSwitchCurrentUnit'
_H='TPLINK-STACK-MIB'
_G='ifIndex'
_F='IF-MIB'
_E='read-write'
_D='DisplayString'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_F,_G)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
tplinkStackMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,34))
if mibBuilder.loadTexts:tplinkStackMIB.setRevisions(('2012-11-29 00:00',))
_TplinkStackMIBObjects_ObjectIdentity=ObjectIdentity
tplinkStackMIBObjects=_TplinkStackMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,34,1))
_TpStackGlobal_ObjectIdentity=ObjectIdentity
tpStackGlobal=_TpStackGlobal_ObjectIdentity((1,3,6,1,4,1,11863,6,34,1,1))
class _TpStackName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TpStackName_Type.__name__=_D
_TpStackName_Object=MibScalar
tpStackName=_TpStackName_Object((1,3,6,1,4,1,11863,6,34,1,1,1),_TpStackName_Type())
tpStackName.setMaxAccess(_E)
if mibBuilder.loadTexts:tpStackName.setStatus(_A)
class _TpStackMacAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TpStackMacAddress_Type.__name__=_D
_TpStackMacAddress_Object=MibScalar
tpStackMacAddress=_TpStackMacAddress_Object((1,3,6,1,4,1,11863,6,34,1,1,2),_TpStackMacAddress_Type())
tpStackMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:tpStackMacAddress.setStatus(_A)
class _TpStackTopo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('line',0),('ring',1)))
_TpStackTopo_Type.__name__=_B
_TpStackTopo_Object=MibScalar
tpStackTopo=_TpStackTopo_Object((1,3,6,1,4,1,11863,6,34,1,1,3),_TpStackTopo_Type())
tpStackTopo.setMaxAccess(_C)
if mibBuilder.loadTexts:tpStackTopo.setStatus(_A)
class _TpStackAuthMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('simple',1),('md5',2)))
_TpStackAuthMode_Type.__name__=_B
_TpStackAuthMode_Object=MibScalar
tpStackAuthMode=_TpStackAuthMode_Object((1,3,6,1,4,1,11863,6,34,1,1,4),_TpStackAuthMode_Type())
tpStackAuthMode.setMaxAccess(_E)
if mibBuilder.loadTexts:tpStackAuthMode.setStatus(_A)
class _TpStackAuthKey_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TpStackAuthKey_Type.__name__=_D
_TpStackAuthKey_Object=MibScalar
tpStackAuthKey=_TpStackAuthKey_Object((1,3,6,1,4,1,11863,6,34,1,1,5),_TpStackAuthKey_Type())
tpStackAuthKey.setMaxAccess(_E)
if mibBuilder.loadTexts:tpStackAuthKey.setStatus(_A)
_TpStackInfo_ObjectIdentity=ObjectIdentity
tpStackInfo=_TpStackInfo_ObjectIdentity((1,3,6,1,4,1,11863,6,34,1,2))
_TpSwitchInfoTable_Object=MibTable
tpSwitchInfoTable=_TpSwitchInfoTable_Object((1,3,6,1,4,1,11863,6,34,1,2,1))
if mibBuilder.loadTexts:tpSwitchInfoTable.setStatus(_A)
_TpSwitchInfoEntry_Object=MibTableRow
tpSwitchInfoEntry=_TpSwitchInfoEntry_Object((1,3,6,1,4,1,11863,6,34,1,2,1,1))
tpSwitchInfoEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:tpSwitchInfoEntry.setStatus(_A)
class _TpSwitchCurrentUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3),(_M,4),(_N,5),(_O,6),(_P,7),(_Q,8)))
_TpSwitchCurrentUnit_Type.__name__=_B
_TpSwitchCurrentUnit_Object=MibTableColumn
tpSwitchCurrentUnit=_TpSwitchCurrentUnit_Object((1,3,6,1,4,1,11863,6,34,1,2,1,1,1),_TpSwitchCurrentUnit_Type())
tpSwitchCurrentUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:tpSwitchCurrentUnit.setStatus(_A)
class _TpSwitchDesignatedUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('auto',-1),(_J,1),(_K,2),(_L,3),(_M,4),(_N,5),(_O,6),(_P,7),(_Q,8)))
_TpSwitchDesignatedUnit_Type.__name__=_B
_TpSwitchDesignatedUnit_Object=MibTableColumn
tpSwitchDesignatedUnit=_TpSwitchDesignatedUnit_Object((1,3,6,1,4,1,11863,6,34,1,2,1,1,3),_TpSwitchDesignatedUnit_Type())
tpSwitchDesignatedUnit.setMaxAccess(_E)
if mibBuilder.loadTexts:tpSwitchDesignatedUnit.setStatus(_A)
class _TpSwitchRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('slave',0),('master',1)))
_TpSwitchRole_Type.__name__=_B
_TpSwitchRole_Object=MibTableColumn
tpSwitchRole=_TpSwitchRole_Object((1,3,6,1,4,1,11863,6,34,1,2,1,1,4),_TpSwitchRole_Type())
tpSwitchRole.setMaxAccess(_C)
if mibBuilder.loadTexts:tpSwitchRole.setStatus(_A)
class _TpSwitchPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_TpSwitchPriority_Type.__name__=_B
_TpSwitchPriority_Object=MibTableColumn
tpSwitchPriority=_TpSwitchPriority_Object((1,3,6,1,4,1,11863,6,34,1,2,1,1,5),_TpSwitchPriority_Type())
tpSwitchPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:tpSwitchPriority.setStatus(_A)
class _TpSwitchMacAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TpSwitchMacAddress_Type.__name__=_D
_TpSwitchMacAddress_Object=MibTableColumn
tpSwitchMacAddress=_TpSwitchMacAddress_Object((1,3,6,1,4,1,11863,6,34,1,2,1,1,6),_TpSwitchMacAddress_Type())
tpSwitchMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:tpSwitchMacAddress.setStatus(_A)
class _TpSwitchVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TpSwitchVersion_Type.__name__=_D
_TpSwitchVersion_Object=MibTableColumn
tpSwitchVersion=_TpSwitchVersion_Object((1,3,6,1,4,1,11863,6,34,1,2,1,1,7),_TpSwitchVersion_Type())
tpSwitchVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:tpSwitchVersion.setStatus(_A)
class _TpSwitchState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('init',1),('disc',2),('sync',3),('ready',4),('verMismatch',5)))
_TpSwitchState_Type.__name__=_B
_TpSwitchState_Object=MibTableColumn
tpSwitchState=_TpSwitchState_Object((1,3,6,1,4,1,11863,6,34,1,2,1,1,8),_TpSwitchState_Type())
tpSwitchState.setMaxAccess(_C)
if mibBuilder.loadTexts:tpSwitchState.setStatus(_A)
_TpStackPortInfoTable_Object=MibTable
tpStackPortInfoTable=_TpStackPortInfoTable_Object((1,3,6,1,4,1,11863,6,34,1,2,2))
if mibBuilder.loadTexts:tpStackPortInfoTable.setStatus(_A)
_TpStackPortInfoEntry_Object=MibTableRow
tpStackPortInfoEntry=_TpStackPortInfoEntry_Object((1,3,6,1,4,1,11863,6,34,1,2,2,1))
tpStackPortInfoEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:tpStackPortInfoEntry.setStatus(_A)
class _TpStackPortEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),('enable',1)))
_TpStackPortEnable_Type.__name__=_B
_TpStackPortEnable_Object=MibTableColumn
tpStackPortEnable=_TpStackPortEnable_Object((1,3,6,1,4,1,11863,6,34,1,2,2,1,1),_TpStackPortEnable_Type())
tpStackPortEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:tpStackPortEnable.setStatus(_A)
class _TpStackPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ok',1),('down',2),('authFail',3),('ethernet',4)))
_TpStackPortStatus_Type.__name__=_B
_TpStackPortStatus_Object=MibTableColumn
tpStackPortStatus=_TpStackPortStatus_Object((1,3,6,1,4,1,11863,6,34,1,2,2,1,2),_TpStackPortStatus_Type())
tpStackPortStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tpStackPortStatus.setStatus(_A)
class _TpStackPortNeighbor_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TpStackPortNeighbor_Type.__name__=_D
_TpStackPortNeighbor_Object=MibTableColumn
tpStackPortNeighbor=_TpStackPortNeighbor_Object((1,3,6,1,4,1,11863,6,34,1,2,2,1,3),_TpStackPortNeighbor_Type())
tpStackPortNeighbor.setMaxAccess(_C)
if mibBuilder.loadTexts:tpStackPortNeighbor.setStatus(_A)
_TplinkStackNotifications_ObjectIdentity=ObjectIdentity
tplinkStackNotifications=_TplinkStackNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,34,2))
mibBuilder.exportSymbols(_H,**{'tplinkStackMIB':tplinkStackMIB,'tplinkStackMIBObjects':tplinkStackMIBObjects,'tpStackGlobal':tpStackGlobal,'tpStackName':tpStackName,'tpStackMacAddress':tpStackMacAddress,'tpStackTopo':tpStackTopo,'tpStackAuthMode':tpStackAuthMode,'tpStackAuthKey':tpStackAuthKey,'tpStackInfo':tpStackInfo,'tpSwitchInfoTable':tpSwitchInfoTable,'tpSwitchInfoEntry':tpSwitchInfoEntry,_I:tpSwitchCurrentUnit,'tpSwitchDesignatedUnit':tpSwitchDesignatedUnit,'tpSwitchRole':tpSwitchRole,'tpSwitchPriority':tpSwitchPriority,'tpSwitchMacAddress':tpSwitchMacAddress,'tpSwitchVersion':tpSwitchVersion,'tpSwitchState':tpSwitchState,'tpStackPortInfoTable':tpStackPortInfoTable,'tpStackPortInfoEntry':tpStackPortInfoEntry,'tpStackPortEnable':tpStackPortEnable,'tpStackPortStatus':tpStackPortStatus,'tpStackPortNeighbor':tpStackPortNeighbor,'tplinkStackNotifications':tplinkStackNotifications})