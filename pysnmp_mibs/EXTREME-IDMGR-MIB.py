_Y='extremeIdMgrEffectiveStaleAgingTime'
_X='extremeIdMgrMemMaxSize'
_W='extremeIdMgrMemUsage'
_V='extremeIdMgrMemUsageLevel'
_U='extremeIdMgrTrapSeverity'
_T='extremeLocationDetectMethod'
_S='netloginDot1x'
_R='netloginWeb'
_Q='netloginMac'
_P='kerberos'
_O='fdbLearn'
_N='critical'
_M='extremeLocationInetAddr'
_L='extremeLocationInetAddrType'
_K='ipArp'
_J='extremeLocationVlanIfIndex'
_I='dhcpSnooping'
_H='Integer32'
_G='not-accessible'
_F='accessible-for-notify'
_E='extremeLocationInterface'
_D='extremeLocationMacAddress'
_C='read-only'
_B='EXTREME-IDMGR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
extremeAgent,=mibBuilder.importSymbols('EXTREME-BASE-MIB','extremeAgent')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
AutonomousType,DateAndTime,DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','AutonomousType','DateAndTime','DisplayString','MacAddress','PhysAddress','TextualConvention')
extremeIdMgr=ModuleIdentity((1,3,6,1,4,1,1916,1,36))
class ExtremeIdMgrInetAddrDetectMethod(TextualConvention,Bits):status=_A;namedValues=NamedValues(*((_K,1),(_I,2)))
class ExtremeIdMgrInetAddrSecViolation(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('arp',1),('dos',2),('garp',3),('srcIpLockdown',4),(_I,5)))
_ExtremeIdMgrTraps_ObjectIdentity=ObjectIdentity
extremeIdMgrTraps=_ExtremeIdMgrTraps_ObjectIdentity((1,3,6,1,4,1,1916,1,36,1))
_ExtremeIdMgrTrapPrefix_ObjectIdentity=ObjectIdentity
extremeIdMgrTrapPrefix=_ExtremeIdMgrTrapPrefix_ObjectIdentity((1,3,6,1,4,1,1916,1,36,1,0))
class _ExtremeIdMgrTrapSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_N,1),('error',2),('warning',3),('notice',4),('info',5),('debug-summary',6),('debug-verbose',7),('debug-data',8)))
_ExtremeIdMgrTrapSeverity_Type.__name__=_H
_ExtremeIdMgrTrapSeverity_Object=MibScalar
extremeIdMgrTrapSeverity=_ExtremeIdMgrTrapSeverity_Object((1,3,6,1,4,1,1916,1,36,1,1),_ExtremeIdMgrTrapSeverity_Type())
extremeIdMgrTrapSeverity.setMaxAccess(_F)
if mibBuilder.loadTexts:extremeIdMgrTrapSeverity.setStatus(_A)
class _ExtremeIdMgrMemUsageLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('normal',1),('high',2),(_N,3),('maximum',4)))
_ExtremeIdMgrMemUsageLevel_Type.__name__=_H
_ExtremeIdMgrMemUsageLevel_Object=MibScalar
extremeIdMgrMemUsageLevel=_ExtremeIdMgrMemUsageLevel_Object((1,3,6,1,4,1,1916,1,36,1,2),_ExtremeIdMgrMemUsageLevel_Type())
extremeIdMgrMemUsageLevel.setMaxAccess(_F)
if mibBuilder.loadTexts:extremeIdMgrMemUsageLevel.setStatus(_A)
_ExtremeIdMgrMemUsage_Type=Integer32
_ExtremeIdMgrMemUsage_Object=MibScalar
extremeIdMgrMemUsage=_ExtremeIdMgrMemUsage_Object((1,3,6,1,4,1,1916,1,36,1,3),_ExtremeIdMgrMemUsage_Type())
extremeIdMgrMemUsage.setMaxAccess(_F)
if mibBuilder.loadTexts:extremeIdMgrMemUsage.setStatus(_A)
_ExtremeIdMgrMemMaxSize_Type=Integer32
_ExtremeIdMgrMemMaxSize_Object=MibScalar
extremeIdMgrMemMaxSize=_ExtremeIdMgrMemMaxSize_Object((1,3,6,1,4,1,1916,1,36,1,4),_ExtremeIdMgrMemMaxSize_Type())
extremeIdMgrMemMaxSize.setMaxAccess(_F)
if mibBuilder.loadTexts:extremeIdMgrMemMaxSize.setStatus(_A)
_ExtremeIdMgrEffectiveStaleAgingTime_Type=Integer32
_ExtremeIdMgrEffectiveStaleAgingTime_Object=MibScalar
extremeIdMgrEffectiveStaleAgingTime=_ExtremeIdMgrEffectiveStaleAgingTime_Object((1,3,6,1,4,1,1916,1,36,1,5),_ExtremeIdMgrEffectiveStaleAgingTime_Type())
extremeIdMgrEffectiveStaleAgingTime.setMaxAccess(_F)
if mibBuilder.loadTexts:extremeIdMgrEffectiveStaleAgingTime.setStatus(_A)
_ExtremeIdMgrObjects_ObjectIdentity=ObjectIdentity
extremeIdMgrObjects=_ExtremeIdMgrObjects_ObjectIdentity((1,3,6,1,4,1,1916,1,36,2))
_ExtremeLocationTable_Object=MibTable
extremeLocationTable=_ExtremeLocationTable_Object((1,3,6,1,4,1,1916,1,36,2,1))
if mibBuilder.loadTexts:extremeLocationTable.setStatus(_A)
_ExtremeLocationEntry_Object=MibTableRow
extremeLocationEntry=_ExtremeLocationEntry_Object((1,3,6,1,4,1,1916,1,36,2,1,1))
extremeLocationEntry.setIndexNames((0,_B,_D),(0,_B,_E))
if mibBuilder.loadTexts:extremeLocationEntry.setStatus(_A)
_ExtremeLocationMacAddress_Type=MacAddress
_ExtremeLocationMacAddress_Object=MibTableColumn
extremeLocationMacAddress=_ExtremeLocationMacAddress_Object((1,3,6,1,4,1,1916,1,36,2,1,1,1),_ExtremeLocationMacAddress_Type())
extremeLocationMacAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:extremeLocationMacAddress.setStatus(_A)
_ExtremeLocationInterface_Type=InterfaceIndex
_ExtremeLocationInterface_Object=MibTableColumn
extremeLocationInterface=_ExtremeLocationInterface_Object((1,3,6,1,4,1,1916,1,36,2,1,1,2),_ExtremeLocationInterface_Type())
extremeLocationInterface.setMaxAccess(_G)
if mibBuilder.loadTexts:extremeLocationInterface.setStatus(_A)
class _ExtremeLocationDetectMethods_Type(Bits):namedValues=NamedValues(*((_O,1),(_K,2),(_I,3),('lldp',4),(_P,5),(_Q,6),(_R,7),(_S,8)))
_ExtremeLocationDetectMethods_Type.__name__='Bits'
_ExtremeLocationDetectMethods_Object=MibTableColumn
extremeLocationDetectMethods=_ExtremeLocationDetectMethods_Object((1,3,6,1,4,1,1916,1,36,2,1,1,3),_ExtremeLocationDetectMethods_Type())
extremeLocationDetectMethods.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeLocationDetectMethods.setStatus(_A)
_ExtremeLocationDetectTime_Type=DateAndTime
_ExtremeLocationDetectTime_Object=MibTableColumn
extremeLocationDetectTime=_ExtremeLocationDetectTime_Object((1,3,6,1,4,1,1916,1,36,2,1,1,4),_ExtremeLocationDetectTime_Type())
extremeLocationDetectTime.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeLocationDetectTime.setStatus(_A)
_ExtremeLocationDetectMethodTable_Object=MibTable
extremeLocationDetectMethodTable=_ExtremeLocationDetectMethodTable_Object((1,3,6,1,4,1,1916,1,36,2,2))
if mibBuilder.loadTexts:extremeLocationDetectMethodTable.setStatus(_A)
_ExtremeLocationDetectMethodEntry_Object=MibTableRow
extremeLocationDetectMethodEntry=_ExtremeLocationDetectMethodEntry_Object((1,3,6,1,4,1,1916,1,36,2,2,1))
extremeLocationDetectMethodEntry.setIndexNames((0,_B,_T),(0,_B,_D),(0,_B,_E))
if mibBuilder.loadTexts:extremeLocationDetectMethodEntry.setStatus(_A)
class _ExtremeLocationDetectMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_O,1),(_K,2),(_I,3),('lldp',4),(_P,5),(_Q,6),(_R,7),(_S,8)))
_ExtremeLocationDetectMethod_Type.__name__=_H
_ExtremeLocationDetectMethod_Object=MibTableColumn
extremeLocationDetectMethod=_ExtremeLocationDetectMethod_Object((1,3,6,1,4,1,1916,1,36,2,2,1,1),_ExtremeLocationDetectMethod_Type())
extremeLocationDetectMethod.setMaxAccess(_G)
if mibBuilder.loadTexts:extremeLocationDetectMethod.setStatus(_A)
_ExtremeLocationDetectMethodData_Type=AutonomousType
_ExtremeLocationDetectMethodData_Object=MibTableColumn
extremeLocationDetectMethodData=_ExtremeLocationDetectMethodData_Object((1,3,6,1,4,1,1916,1,36,2,2,1,2),_ExtremeLocationDetectMethodData_Type())
extremeLocationDetectMethodData.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeLocationDetectMethodData.setStatus(_A)
_ExtremeLocationVlanTable_Object=MibTable
extremeLocationVlanTable=_ExtremeLocationVlanTable_Object((1,3,6,1,4,1,1916,1,36,2,3))
if mibBuilder.loadTexts:extremeLocationVlanTable.setStatus(_A)
_ExtremeLocationVlanEntry_Object=MibTableRow
extremeLocationVlanEntry=_ExtremeLocationVlanEntry_Object((1,3,6,1,4,1,1916,1,36,2,3,1))
extremeLocationVlanEntry.setIndexNames((0,_B,_D),(0,_B,_E),(0,_B,_J))
if mibBuilder.loadTexts:extremeLocationVlanEntry.setStatus(_A)
_ExtremeLocationVlanIfIndex_Type=InterfaceIndex
_ExtremeLocationVlanIfIndex_Object=MibTableColumn
extremeLocationVlanIfIndex=_ExtremeLocationVlanIfIndex_Object((1,3,6,1,4,1,1916,1,36,2,3,1,1),_ExtremeLocationVlanIfIndex_Type())
extremeLocationVlanIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeLocationVlanIfIndex.setStatus(_A)
_ExtremeLocationInetAddrTable_Object=MibTable
extremeLocationInetAddrTable=_ExtremeLocationInetAddrTable_Object((1,3,6,1,4,1,1916,1,36,2,4))
if mibBuilder.loadTexts:extremeLocationInetAddrTable.setStatus(_A)
_ExtremeLocationInetAddrEntry_Object=MibTableRow
extremeLocationInetAddrEntry=_ExtremeLocationInetAddrEntry_Object((1,3,6,1,4,1,1916,1,36,2,4,1))
extremeLocationInetAddrEntry.setIndexNames((0,_B,_D),(0,_B,_E),(0,_B,_J),(0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:extremeLocationInetAddrEntry.setStatus(_A)
_ExtremeLocationInetAddrType_Type=InetAddressType
_ExtremeLocationInetAddrType_Object=MibTableColumn
extremeLocationInetAddrType=_ExtremeLocationInetAddrType_Object((1,3,6,1,4,1,1916,1,36,2,4,1,1),_ExtremeLocationInetAddrType_Type())
extremeLocationInetAddrType.setMaxAccess(_G)
if mibBuilder.loadTexts:extremeLocationInetAddrType.setStatus(_A)
_ExtremeLocationInetAddr_Type=InetAddress
_ExtremeLocationInetAddr_Object=MibTableColumn
extremeLocationInetAddr=_ExtremeLocationInetAddr_Object((1,3,6,1,4,1,1916,1,36,2,4,1,2),_ExtremeLocationInetAddr_Type())
extremeLocationInetAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:extremeLocationInetAddr.setStatus(_A)
_ExtremeLocationInetAddrDetectMethod_Type=ExtremeIdMgrInetAddrDetectMethod
_ExtremeLocationInetAddrDetectMethod_Object=MibTableColumn
extremeLocationInetAddrDetectMethod=_ExtremeLocationInetAddrDetectMethod_Object((1,3,6,1,4,1,1916,1,36,2,4,1,3),_ExtremeLocationInetAddrDetectMethod_Type())
extremeLocationInetAddrDetectMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeLocationInetAddrDetectMethod.setStatus(_A)
_ExtremeLocationInetAddrSecViolations_Type=ExtremeIdMgrInetAddrSecViolation
_ExtremeLocationInetAddrSecViolations_Object=MibTableColumn
extremeLocationInetAddrSecViolations=_ExtremeLocationInetAddrSecViolations_Object((1,3,6,1,4,1,1916,1,36,2,4,1,4),_ExtremeLocationInetAddrSecViolations_Type())
extremeLocationInetAddrSecViolations.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeLocationInetAddrSecViolations.setStatus(_A)
_ExtremeLocationInetAddrInvTable_Object=MibTable
extremeLocationInetAddrInvTable=_ExtremeLocationInetAddrInvTable_Object((1,3,6,1,4,1,1916,1,36,2,5))
if mibBuilder.loadTexts:extremeLocationInetAddrInvTable.setStatus(_A)
_ExtremeLocationInetAddrInvEntry_Object=MibTableRow
extremeLocationInetAddrInvEntry=_ExtremeLocationInetAddrInvEntry_Object((1,3,6,1,4,1,1916,1,36,2,5,1))
extremeLocationInetAddrInvEntry.setIndexNames((0,_B,_L),(0,_B,_M),(0,_B,_J),(0,_B,_E),(0,_B,_D))
if mibBuilder.loadTexts:extremeLocationInetAddrInvEntry.setStatus(_A)
_ExtremeLocationInetAddrInvDetectMethod_Type=ExtremeIdMgrInetAddrDetectMethod
_ExtremeLocationInetAddrInvDetectMethod_Object=MibTableColumn
extremeLocationInetAddrInvDetectMethod=_ExtremeLocationInetAddrInvDetectMethod_Object((1,3,6,1,4,1,1916,1,36,2,5,1,1),_ExtremeLocationInetAddrInvDetectMethod_Type())
extremeLocationInetAddrInvDetectMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeLocationInetAddrInvDetectMethod.setStatus(_A)
_ExtremeLocationInetAddrInvSecViolations_Type=ExtremeIdMgrInetAddrSecViolation
_ExtremeLocationInetAddrInvSecViolations_Object=MibTableColumn
extremeLocationInetAddrInvSecViolations=_ExtremeLocationInetAddrInvSecViolations_Object((1,3,6,1,4,1,1916,1,36,2,5,1,2),_ExtremeLocationInetAddrInvSecViolations_Type())
extremeLocationInetAddrInvSecViolations.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeLocationInetAddrInvSecViolations.setStatus(_A)
_ExtremeIdMgrConformance_ObjectIdentity=ObjectIdentity
extremeIdMgrConformance=_ExtremeIdMgrConformance_ObjectIdentity((1,3,6,1,4,1,1916,1,36,3))
extremeIdMgrMemLevelChange=NotificationType((1,3,6,1,4,1,1916,1,36,1,0,1))
extremeIdMgrMemLevelChange.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:extremeIdMgrMemLevelChange.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ExtremeIdMgrInetAddrDetectMethod':ExtremeIdMgrInetAddrDetectMethod,'ExtremeIdMgrInetAddrSecViolation':ExtremeIdMgrInetAddrSecViolation,'extremeIdMgr':extremeIdMgr,'extremeIdMgrTraps':extremeIdMgrTraps,'extremeIdMgrTrapPrefix':extremeIdMgrTrapPrefix,'extremeIdMgrMemLevelChange':extremeIdMgrMemLevelChange,_U:extremeIdMgrTrapSeverity,_V:extremeIdMgrMemUsageLevel,_W:extremeIdMgrMemUsage,_X:extremeIdMgrMemMaxSize,_Y:extremeIdMgrEffectiveStaleAgingTime,'extremeIdMgrObjects':extremeIdMgrObjects,'extremeLocationTable':extremeLocationTable,'extremeLocationEntry':extremeLocationEntry,_D:extremeLocationMacAddress,_E:extremeLocationInterface,'extremeLocationDetectMethods':extremeLocationDetectMethods,'extremeLocationDetectTime':extremeLocationDetectTime,'extremeLocationDetectMethodTable':extremeLocationDetectMethodTable,'extremeLocationDetectMethodEntry':extremeLocationDetectMethodEntry,_T:extremeLocationDetectMethod,'extremeLocationDetectMethodData':extremeLocationDetectMethodData,'extremeLocationVlanTable':extremeLocationVlanTable,'extremeLocationVlanEntry':extremeLocationVlanEntry,_J:extremeLocationVlanIfIndex,'extremeLocationInetAddrTable':extremeLocationInetAddrTable,'extremeLocationInetAddrEntry':extremeLocationInetAddrEntry,_L:extremeLocationInetAddrType,_M:extremeLocationInetAddr,'extremeLocationInetAddrDetectMethod':extremeLocationInetAddrDetectMethod,'extremeLocationInetAddrSecViolations':extremeLocationInetAddrSecViolations,'extremeLocationInetAddrInvTable':extremeLocationInetAddrInvTable,'extremeLocationInetAddrInvEntry':extremeLocationInetAddrInvEntry,'extremeLocationInetAddrInvDetectMethod':extremeLocationInetAddrInvDetectMethod,'extremeLocationInetAddrInvSecViolations':extremeLocationInetAddrInvSecViolations,'extremeIdMgrConformance':extremeIdMgrConformance})