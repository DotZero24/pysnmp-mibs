_m='os10PortSecuritySecureMacAddrGroup'
_l='os10PortSecurityInterfaceGroup'
_k='os10PortSecurityGlobalGroup'
_j='os10PortSecuritySecureMacAddrType'
_i='os10PortSecuritySecureMacIfIndex'
_h='os10PortSecurityIfClearSecureMacAddresses'
_g='os10PortSecurityIfTotalSecureStaticAddresses'
_f='os10PortSecurityIfTotalSecureStickyAddresses'
_e='os10PortSecurityIfTotalSecureDynamicAddresses'
_d='os10PortSecurityIfTotalSecureAddresses'
_c='os10PortSecurityIfSecureMacAgeEnable'
_b='os10PortSecurityIfStickyEnable'
_a='os10PortSecurityIfStmvViolationAction'
_Z='os10PortSecurityIfMacViolationAction'
_Y='os10PortSecurityIfStationMoveEnable'
_X='os10PortSecurityIfSecureMacLearnLimit'
_W='os10PortSecurityIfViolationStatus'
_V='os10PortSecurityIfPortSecurityEnable'
_U='os10PortSecurityGlobalResetViolation'
_T='os10PortSecurityGlobalClearSecureMacAddresses'
_S='os10PortSecurityGlobalTotalSecureStaticAddresses'
_R='os10PortSecurityGlobalTotalSecureStickyAddresses'
_Q='os10PortSecurityGlobalTotalSecureDynamicAddresses'
_P='os10PortSecurityGlobalTotalSecureAddresses'
_O='os10PortSecurityGlobalEnable'
_N='os10PortSecuritySecureMacAddress'
_M='os10PortSecuritySecureMacVlanId'
_L='dropAndNotify'
_K='os10PortSecurityIfIndex'
_J='sticky'
_I='dynamic'
_H='Unsigned32'
_G='not-accessible'
_F='TruthValue'
_E='read-only'
_D='read-write'
_C='Integer32'
_B='DELLEMC-OS10-PORT-SECURITY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
os10,=mibBuilder.importSymbols('DELLEMC-OS10-SMI-MIB','os10')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
VlanIndex,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention',_F)
os10PortSecurityMib=ModuleIdentity((1,3,6,1,4,1,674,11000,5000,100,5))
if mibBuilder.loadTexts:os10PortSecurityMib.setRevisions(('2019-07-22 00:00',))
class SecureMacAddrType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),(_I,1),(_J,2),('all',3)))
class SecureMacViolationType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('macLimitViolation',1),('stmvViolation',2)))
_Os10PortSecurityMibObjects_ObjectIdentity=ObjectIdentity
os10PortSecurityMibObjects=_Os10PortSecurityMibObjects_ObjectIdentity((1,3,6,1,4,1,674,11000,5000,100,5,1))
_Os10PortSecurityGlobalObjects_ObjectIdentity=ObjectIdentity
os10PortSecurityGlobalObjects=_Os10PortSecurityGlobalObjects_ObjectIdentity((1,3,6,1,4,1,674,11000,5000,100,5,1,1))
class _Os10PortSecurityGlobalEnable_Type(TruthValue):defaultValue=1
_Os10PortSecurityGlobalEnable_Type.__name__=_F
_Os10PortSecurityGlobalEnable_Object=MibScalar
os10PortSecurityGlobalEnable=_Os10PortSecurityGlobalEnable_Object((1,3,6,1,4,1,674,11000,5000,100,5,1,1,1),_Os10PortSecurityGlobalEnable_Type())
os10PortSecurityGlobalEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:os10PortSecurityGlobalEnable.setStatus(_A)
class _Os10PortSecurityGlobalTotalSecureAddresses_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Os10PortSecurityGlobalTotalSecureAddresses_Type.__name__=_C
_Os10PortSecurityGlobalTotalSecureAddresses_Object=MibScalar
os10PortSecurityGlobalTotalSecureAddresses=_Os10PortSecurityGlobalTotalSecureAddresses_Object((1,3,6,1,4,1,674,11000,5000,100,5,1,1,2),_Os10PortSecurityGlobalTotalSecureAddresses_Type())
os10PortSecurityGlobalTotalSecureAddresses.setMaxAccess(_E)
if mibBuilder.loadTexts:os10PortSecurityGlobalTotalSecureAddresses.setStatus(_A)
class _Os10PortSecurityGlobalTotalSecureDynamicAddresses_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Os10PortSecurityGlobalTotalSecureDynamicAddresses_Type.__name__=_C
_Os10PortSecurityGlobalTotalSecureDynamicAddresses_Object=MibScalar
os10PortSecurityGlobalTotalSecureDynamicAddresses=_Os10PortSecurityGlobalTotalSecureDynamicAddresses_Object((1,3,6,1,4,1,674,11000,5000,100,5,1,1,3),_Os10PortSecurityGlobalTotalSecureDynamicAddresses_Type())
os10PortSecurityGlobalTotalSecureDynamicAddresses.setMaxAccess(_E)
if mibBuilder.loadTexts:os10PortSecurityGlobalTotalSecureDynamicAddresses.setStatus(_A)
class _Os10PortSecurityGlobalTotalSecureStickyAddresses_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Os10PortSecurityGlobalTotalSecureStickyAddresses_Type.__name__=_C
_Os10PortSecurityGlobalTotalSecureStickyAddresses_Object=MibScalar
os10PortSecurityGlobalTotalSecureStickyAddresses=_Os10PortSecurityGlobalTotalSecureStickyAddresses_Object((1,3,6,1,4,1,674,11000,5000,100,5,1,1,4),_Os10PortSecurityGlobalTotalSecureStickyAddresses_Type())
os10PortSecurityGlobalTotalSecureStickyAddresses.setMaxAccess(_E)
if mibBuilder.loadTexts:os10PortSecurityGlobalTotalSecureStickyAddresses.setStatus(_A)
class _Os10PortSecurityGlobalTotalSecureStaticAddresses_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Os10PortSecurityGlobalTotalSecureStaticAddresses_Type.__name__=_C
_Os10PortSecurityGlobalTotalSecureStaticAddresses_Object=MibScalar
os10PortSecurityGlobalTotalSecureStaticAddresses=_Os10PortSecurityGlobalTotalSecureStaticAddresses_Object((1,3,6,1,4,1,674,11000,5000,100,5,1,1,5),_Os10PortSecurityGlobalTotalSecureStaticAddresses_Type())
os10PortSecurityGlobalTotalSecureStaticAddresses.setMaxAccess(_E)
if mibBuilder.loadTexts:os10PortSecurityGlobalTotalSecureStaticAddresses.setStatus(_A)
_Os10PortSecurityGlobalClearSecureMacAddresses_Type=SecureMacAddrType
_Os10PortSecurityGlobalClearSecureMacAddresses_Object=MibScalar
os10PortSecurityGlobalClearSecureMacAddresses=_Os10PortSecurityGlobalClearSecureMacAddresses_Object((1,3,6,1,4,1,674,11000,5000,100,5,1,1,6),_Os10PortSecurityGlobalClearSecureMacAddresses_Type())
os10PortSecurityGlobalClearSecureMacAddresses.setMaxAccess(_D)
if mibBuilder.loadTexts:os10PortSecurityGlobalClearSecureMacAddresses.setStatus(_A)
_Os10PortSecurityGlobalResetViolation_Type=SecureMacViolationType
_Os10PortSecurityGlobalResetViolation_Object=MibScalar
os10PortSecurityGlobalResetViolation=_Os10PortSecurityGlobalResetViolation_Object((1,3,6,1,4,1,674,11000,5000,100,5,1,1,7),_Os10PortSecurityGlobalResetViolation_Type())
os10PortSecurityGlobalResetViolation.setMaxAccess(_D)
if mibBuilder.loadTexts:os10PortSecurityGlobalResetViolation.setStatus(_A)
_Os10PortSecurityInterfaceObjects_ObjectIdentity=ObjectIdentity
os10PortSecurityInterfaceObjects=_Os10PortSecurityInterfaceObjects_ObjectIdentity((1,3,6,1,4,1,674,11000,5000,100,5,1,2))
_Os10PortSecurityIfConfigTable_Object=MibTable
os10PortSecurityIfConfigTable=_Os10PortSecurityIfConfigTable_Object((1,3,6,1,4,1,674,11000,5000,100,5,1,2,1))
if mibBuilder.loadTexts:os10PortSecurityIfConfigTable.setStatus(_A)
_Os10PortSecurityIfConfigEntry_Object=MibTableRow
os10PortSecurityIfConfigEntry=_Os10PortSecurityIfConfigEntry_Object((1,3,6,1,4,1,674,11000,5000,100,5,1,2,1,1))
os10PortSecurityIfConfigEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:os10PortSecurityIfConfigEntry.setStatus(_A)
_Os10PortSecurityIfIndex_Type=InterfaceIndex
_Os10PortSecurityIfIndex_Object=MibTableColumn
os10PortSecurityIfIndex=_Os10PortSecurityIfIndex_Object((1,3,6,1,4,1,674,11000,5000,100,5,1,2,1,1,1),_Os10PortSecurityIfIndex_Type())
os10PortSecurityIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:os10PortSecurityIfIndex.setStatus(_A)
class _Os10PortSecurityIfPortSecurityEnable_Type(TruthValue):defaultValue=2
_Os10PortSecurityIfPortSecurityEnable_Type.__name__=_F
_Os10PortSecurityIfPortSecurityEnable_Object=MibTableColumn
os10PortSecurityIfPortSecurityEnable=_Os10PortSecurityIfPortSecurityEnable_Object((1,3,6,1,4,1,674,11000,5000,100,5,1,2,1,1,2),_Os10PortSecurityIfPortSecurityEnable_Type())
os10PortSecurityIfPortSecurityEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:os10PortSecurityIfPortSecurityEnable.setStatus(_A)
class _Os10PortSecurityIfViolationStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('normal',1),('macLearnLimitErrDisable',2),('stationMoveErrDisable',3)))
_Os10PortSecurityIfViolationStatus_Type.__name__=_C
_Os10PortSecurityIfViolationStatus_Object=MibTableColumn
os10PortSecurityIfViolationStatus=_Os10PortSecurityIfViolationStatus_Object((1,3,6,1,4,1,674,11000,5000,100,5,1,2,1,1,3),_Os10PortSecurityIfViolationStatus_Type())
os10PortSecurityIfViolationStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:os10PortSecurityIfViolationStatus.setStatus(_A)
class _Os10PortSecurityIfSecureMacLearnLimit_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_Os10PortSecurityIfSecureMacLearnLimit_Type.__name__=_H
_Os10PortSecurityIfSecureMacLearnLimit_Object=MibTableColumn
os10PortSecurityIfSecureMacLearnLimit=_Os10PortSecurityIfSecureMacLearnLimit_Object((1,3,6,1,4,1,674,11000,5000,100,5,1,2,1,1,4),_Os10PortSecurityIfSecureMacLearnLimit_Type())
os10PortSecurityIfSecureMacLearnLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:os10PortSecurityIfSecureMacLearnLimit.setStatus(_A)
class _Os10PortSecurityIfStationMoveEnable_Type(TruthValue):defaultValue=2
_Os10PortSecurityIfStationMoveEnable_Type.__name__=_F
_Os10PortSecurityIfStationMoveEnable_Object=MibTableColumn
os10PortSecurityIfStationMoveEnable=_Os10PortSecurityIfStationMoveEnable_Object((1,3,6,1,4,1,674,11000,5000,100,5,1,2,1,1,5),_Os10PortSecurityIfStationMoveEnable_Type())
os10PortSecurityIfStationMoveEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:os10PortSecurityIfStationMoveEnable.setStatus(_A)
class _Os10PortSecurityIfMacViolationAction_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('drop',1),(_L,2),('shutdown',3),('forward',4)))
_Os10PortSecurityIfMacViolationAction_Type.__name__=_C
_Os10PortSecurityIfMacViolationAction_Object=MibTableColumn
os10PortSecurityIfMacViolationAction=_Os10PortSecurityIfMacViolationAction_Object((1,3,6,1,4,1,674,11000,5000,100,5,1,2,1,1,6),_Os10PortSecurityIfMacViolationAction_Type())
os10PortSecurityIfMacViolationAction.setMaxAccess(_D)
if mibBuilder.loadTexts:os10PortSecurityIfMacViolationAction.setStatus(_A)
class _Os10PortSecurityIfStmvViolationAction_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('drop',1),(_L,2),('shutdownOrigPort',3),('shutDownOffendingPort',4),('shutdownBoth',5)))
_Os10PortSecurityIfStmvViolationAction_Type.__name__=_C
_Os10PortSecurityIfStmvViolationAction_Object=MibTableColumn
os10PortSecurityIfStmvViolationAction=_Os10PortSecurityIfStmvViolationAction_Object((1,3,6,1,4,1,674,11000,5000,100,5,1,2,1,1,7),_Os10PortSecurityIfStmvViolationAction_Type())
os10PortSecurityIfStmvViolationAction.setMaxAccess(_D)
if mibBuilder.loadTexts:os10PortSecurityIfStmvViolationAction.setStatus(_A)
class _Os10PortSecurityIfStickyEnable_Type(TruthValue):defaultValue=2
_Os10PortSecurityIfStickyEnable_Type.__name__=_F
_Os10PortSecurityIfStickyEnable_Object=MibTableColumn
os10PortSecurityIfStickyEnable=_Os10PortSecurityIfStickyEnable_Object((1,3,6,1,4,1,674,11000,5000,100,5,1,2,1,1,8),_Os10PortSecurityIfStickyEnable_Type())
os10PortSecurityIfStickyEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:os10PortSecurityIfStickyEnable.setStatus(_A)
_Os10PortSecurityIfClearSecureMacAddresses_Type=SecureMacAddrType
_Os10PortSecurityIfClearSecureMacAddresses_Object=MibTableColumn
os10PortSecurityIfClearSecureMacAddresses=_Os10PortSecurityIfClearSecureMacAddresses_Object((1,3,6,1,4,1,674,11000,5000,100,5,1,2,1,1,9),_Os10PortSecurityIfClearSecureMacAddresses_Type())
os10PortSecurityIfClearSecureMacAddresses.setMaxAccess(_D)
if mibBuilder.loadTexts:os10PortSecurityIfClearSecureMacAddresses.setStatus(_A)
class _Os10PortSecurityIfSecureMacAgeEnable_Type(TruthValue):defaultValue=2
_Os10PortSecurityIfSecureMacAgeEnable_Type.__name__=_F
_Os10PortSecurityIfSecureMacAgeEnable_Object=MibTableColumn
os10PortSecurityIfSecureMacAgeEnable=_Os10PortSecurityIfSecureMacAgeEnable_Object((1,3,6,1,4,1,674,11000,5000,100,5,1,2,1,1,10),_Os10PortSecurityIfSecureMacAgeEnable_Type())
os10PortSecurityIfSecureMacAgeEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:os10PortSecurityIfSecureMacAgeEnable.setStatus(_A)
class _Os10PortSecurityIfTotalSecureAddresses_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Os10PortSecurityIfTotalSecureAddresses_Type.__name__=_C
_Os10PortSecurityIfTotalSecureAddresses_Object=MibTableColumn
os10PortSecurityIfTotalSecureAddresses=_Os10PortSecurityIfTotalSecureAddresses_Object((1,3,6,1,4,1,674,11000,5000,100,5,1,2,1,1,11),_Os10PortSecurityIfTotalSecureAddresses_Type())
os10PortSecurityIfTotalSecureAddresses.setMaxAccess(_E)
if mibBuilder.loadTexts:os10PortSecurityIfTotalSecureAddresses.setStatus(_A)
class _Os10PortSecurityIfTotalSecureDynamicAddresses_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Os10PortSecurityIfTotalSecureDynamicAddresses_Type.__name__=_C
_Os10PortSecurityIfTotalSecureDynamicAddresses_Object=MibTableColumn
os10PortSecurityIfTotalSecureDynamicAddresses=_Os10PortSecurityIfTotalSecureDynamicAddresses_Object((1,3,6,1,4,1,674,11000,5000,100,5,1,2,1,1,12),_Os10PortSecurityIfTotalSecureDynamicAddresses_Type())
os10PortSecurityIfTotalSecureDynamicAddresses.setMaxAccess(_E)
if mibBuilder.loadTexts:os10PortSecurityIfTotalSecureDynamicAddresses.setStatus(_A)
class _Os10PortSecurityIfTotalSecureStickyAddresses_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Os10PortSecurityIfTotalSecureStickyAddresses_Type.__name__=_C
_Os10PortSecurityIfTotalSecureStickyAddresses_Object=MibTableColumn
os10PortSecurityIfTotalSecureStickyAddresses=_Os10PortSecurityIfTotalSecureStickyAddresses_Object((1,3,6,1,4,1,674,11000,5000,100,5,1,2,1,1,13),_Os10PortSecurityIfTotalSecureStickyAddresses_Type())
os10PortSecurityIfTotalSecureStickyAddresses.setMaxAccess(_E)
if mibBuilder.loadTexts:os10PortSecurityIfTotalSecureStickyAddresses.setStatus(_A)
class _Os10PortSecurityIfTotalSecureStaticAddresses_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Os10PortSecurityIfTotalSecureStaticAddresses_Type.__name__=_C
_Os10PortSecurityIfTotalSecureStaticAddresses_Object=MibTableColumn
os10PortSecurityIfTotalSecureStaticAddresses=_Os10PortSecurityIfTotalSecureStaticAddresses_Object((1,3,6,1,4,1,674,11000,5000,100,5,1,2,1,1,14),_Os10PortSecurityIfTotalSecureStaticAddresses_Type())
os10PortSecurityIfTotalSecureStaticAddresses.setMaxAccess(_E)
if mibBuilder.loadTexts:os10PortSecurityIfTotalSecureStaticAddresses.setStatus(_A)
_Os10PortSecurityMacObjects_ObjectIdentity=ObjectIdentity
os10PortSecurityMacObjects=_Os10PortSecurityMacObjects_ObjectIdentity((1,3,6,1,4,1,674,11000,5000,100,5,1,3))
_Os10PortSecuritySecureMacAddrTable_Object=MibTable
os10PortSecuritySecureMacAddrTable=_Os10PortSecuritySecureMacAddrTable_Object((1,3,6,1,4,1,674,11000,5000,100,5,1,3,1))
if mibBuilder.loadTexts:os10PortSecuritySecureMacAddrTable.setStatus(_A)
_Os10PortSecuritySecureMacAddrEntry_Object=MibTableRow
os10PortSecuritySecureMacAddrEntry=_Os10PortSecuritySecureMacAddrEntry_Object((1,3,6,1,4,1,674,11000,5000,100,5,1,3,1,1))
os10PortSecuritySecureMacAddrEntry.setIndexNames((0,_B,_M),(0,_B,_N))
if mibBuilder.loadTexts:os10PortSecuritySecureMacAddrEntry.setStatus(_A)
_Os10PortSecuritySecureMacVlanId_Type=VlanIndex
_Os10PortSecuritySecureMacVlanId_Object=MibTableColumn
os10PortSecuritySecureMacVlanId=_Os10PortSecuritySecureMacVlanId_Object((1,3,6,1,4,1,674,11000,5000,100,5,1,3,1,1,1),_Os10PortSecuritySecureMacVlanId_Type())
os10PortSecuritySecureMacVlanId.setMaxAccess(_G)
if mibBuilder.loadTexts:os10PortSecuritySecureMacVlanId.setStatus(_A)
_Os10PortSecuritySecureMacAddress_Type=MacAddress
_Os10PortSecuritySecureMacAddress_Object=MibTableColumn
os10PortSecuritySecureMacAddress=_Os10PortSecuritySecureMacAddress_Object((1,3,6,1,4,1,674,11000,5000,100,5,1,3,1,1,2),_Os10PortSecuritySecureMacAddress_Type())
os10PortSecuritySecureMacAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:os10PortSecuritySecureMacAddress.setStatus(_A)
_Os10PortSecuritySecureMacIfIndex_Type=InterfaceIndex
_Os10PortSecuritySecureMacIfIndex_Object=MibTableColumn
os10PortSecuritySecureMacIfIndex=_Os10PortSecuritySecureMacIfIndex_Object((1,3,6,1,4,1,674,11000,5000,100,5,1,3,1,1,3),_Os10PortSecuritySecureMacIfIndex_Type())
os10PortSecuritySecureMacIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:os10PortSecuritySecureMacIfIndex.setStatus(_A)
class _Os10PortSecuritySecureMacAddrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('static',1),(_I,2),(_J,3)))
_Os10PortSecuritySecureMacAddrType_Type.__name__=_C
_Os10PortSecuritySecureMacAddrType_Object=MibTableColumn
os10PortSecuritySecureMacAddrType=_Os10PortSecuritySecureMacAddrType_Object((1,3,6,1,4,1,674,11000,5000,100,5,1,3,1,1,4),_Os10PortSecuritySecureMacAddrType_Type())
os10PortSecuritySecureMacAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:os10PortSecuritySecureMacAddrType.setStatus(_A)
_Os10PortSecurityMibConformance_ObjectIdentity=ObjectIdentity
os10PortSecurityMibConformance=_Os10PortSecurityMibConformance_ObjectIdentity((1,3,6,1,4,1,674,11000,5000,100,5,2))
_Os10PortSecurityCompliances_ObjectIdentity=ObjectIdentity
os10PortSecurityCompliances=_Os10PortSecurityCompliances_ObjectIdentity((1,3,6,1,4,1,674,11000,5000,100,5,2,1))
_Os10PortSecurityGroups_ObjectIdentity=ObjectIdentity
os10PortSecurityGroups=_Os10PortSecurityGroups_ObjectIdentity((1,3,6,1,4,1,674,11000,5000,100,5,2,2))
os10PortSecurityGlobalGroup=ObjectGroup((1,3,6,1,4,1,674,11000,5000,100,5,2,2,1))
os10PortSecurityGlobalGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:os10PortSecurityGlobalGroup.setStatus(_A)
os10PortSecurityInterfaceGroup=ObjectGroup((1,3,6,1,4,1,674,11000,5000,100,5,2,2,2))
os10PortSecurityInterfaceGroup.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:os10PortSecurityInterfaceGroup.setStatus(_A)
os10PortSecuritySecureMacAddrGroup=ObjectGroup((1,3,6,1,4,1,674,11000,5000,100,5,2,2,3))
os10PortSecuritySecureMacAddrGroup.setObjects(*((_B,_i),(_B,_j)))
if mibBuilder.loadTexts:os10PortSecuritySecureMacAddrGroup.setStatus(_A)
os10PortSecurityMibConform=ModuleCompliance((1,3,6,1,4,1,674,11000,5000,100,5,2,1,1))
os10PortSecurityMibConform.setObjects(*((_B,_k),(_B,_l),(_B,_m)))
if mibBuilder.loadTexts:os10PortSecurityMibConform.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'SecureMacAddrType':SecureMacAddrType,'SecureMacViolationType':SecureMacViolationType,'os10PortSecurityMib':os10PortSecurityMib,'os10PortSecurityMibObjects':os10PortSecurityMibObjects,'os10PortSecurityGlobalObjects':os10PortSecurityGlobalObjects,_O:os10PortSecurityGlobalEnable,_P:os10PortSecurityGlobalTotalSecureAddresses,_Q:os10PortSecurityGlobalTotalSecureDynamicAddresses,_R:os10PortSecurityGlobalTotalSecureStickyAddresses,_S:os10PortSecurityGlobalTotalSecureStaticAddresses,_T:os10PortSecurityGlobalClearSecureMacAddresses,_U:os10PortSecurityGlobalResetViolation,'os10PortSecurityInterfaceObjects':os10PortSecurityInterfaceObjects,'os10PortSecurityIfConfigTable':os10PortSecurityIfConfigTable,'os10PortSecurityIfConfigEntry':os10PortSecurityIfConfigEntry,_K:os10PortSecurityIfIndex,_V:os10PortSecurityIfPortSecurityEnable,_W:os10PortSecurityIfViolationStatus,_X:os10PortSecurityIfSecureMacLearnLimit,_Y:os10PortSecurityIfStationMoveEnable,_Z:os10PortSecurityIfMacViolationAction,_a:os10PortSecurityIfStmvViolationAction,_b:os10PortSecurityIfStickyEnable,_h:os10PortSecurityIfClearSecureMacAddresses,_c:os10PortSecurityIfSecureMacAgeEnable,_d:os10PortSecurityIfTotalSecureAddresses,_e:os10PortSecurityIfTotalSecureDynamicAddresses,_f:os10PortSecurityIfTotalSecureStickyAddresses,_g:os10PortSecurityIfTotalSecureStaticAddresses,'os10PortSecurityMacObjects':os10PortSecurityMacObjects,'os10PortSecuritySecureMacAddrTable':os10PortSecuritySecureMacAddrTable,'os10PortSecuritySecureMacAddrEntry':os10PortSecuritySecureMacAddrEntry,_M:os10PortSecuritySecureMacVlanId,_N:os10PortSecuritySecureMacAddress,_i:os10PortSecuritySecureMacIfIndex,_j:os10PortSecuritySecureMacAddrType,'os10PortSecurityMibConformance':os10PortSecurityMibConformance,'os10PortSecurityCompliances':os10PortSecurityCompliances,'os10PortSecurityMibConform':os10PortSecurityMibConform,'os10PortSecurityGroups':os10PortSecurityGroups,_k:os10PortSecurityGlobalGroup,_l:os10PortSecurityInterfaceGroup,_m:os10PortSecuritySecureMacAddrGroup})