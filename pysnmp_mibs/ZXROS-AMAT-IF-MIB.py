_I='zxrosAMATInterfaceStatisticIfIndex'
_H='read-write'
_G='disable'
_F='enable'
_E='zxrosAMATInterfaceEnableIfIndex'
_D='ZXROS-AMAT-IF-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Zte_ObjectIdentity=ObjectIdentity
zte=_Zte_ObjectIdentity((1,3,6,1,4,1,3902))
_Zxros_ObjectIdentity=ObjectIdentity
zxros=_Zxros_ObjectIdentity((1,3,6,1,4,1,3902,100))
_ZxrosAMATIF_ObjectIdentity=ObjectIdentity
zxrosAMATIF=_ZxrosAMATIF_ObjectIdentity((1,3,6,1,4,1,3902,100,1001))
_ZxrosAMATInterfaceEnableTable_Object=MibTable
zxrosAMATInterfaceEnableTable=_ZxrosAMATInterfaceEnableTable_Object((1,3,6,1,4,1,3902,100,1001,1))
if mibBuilder.loadTexts:zxrosAMATInterfaceEnableTable.setStatus(_A)
_ZxrosAMATInterfaceEnableEntry_Object=MibTableRow
zxrosAMATInterfaceEnableEntry=_ZxrosAMATInterfaceEnableEntry_Object((1,3,6,1,4,1,3902,100,1001,1,1))
zxrosAMATInterfaceEnableEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:zxrosAMATInterfaceEnableEntry.setStatus(_A)
_ZxrosAMATInterfaceEnableIfIndex_Type=Integer32
_ZxrosAMATInterfaceEnableIfIndex_Object=MibTableColumn
zxrosAMATInterfaceEnableIfIndex=_ZxrosAMATInterfaceEnableIfIndex_Object((1,3,6,1,4,1,3902,100,1001,1,1,1),_ZxrosAMATInterfaceEnableIfIndex_Type())
zxrosAMATInterfaceEnableIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:zxrosAMATInterfaceEnableIfIndex.setStatus(_A)
class _ZxrosAMATInterfaceInAmatEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_ZxrosAMATInterfaceInAmatEnable_Type.__name__=_C
_ZxrosAMATInterfaceInAmatEnable_Object=MibTableColumn
zxrosAMATInterfaceInAmatEnable=_ZxrosAMATInterfaceInAmatEnable_Object((1,3,6,1,4,1,3902,100,1001,1,1,2),_ZxrosAMATInterfaceInAmatEnable_Type())
zxrosAMATInterfaceInAmatEnable.setMaxAccess(_H)
if mibBuilder.loadTexts:zxrosAMATInterfaceInAmatEnable.setStatus(_A)
class _ZxrosAMATInterfaceOutAmatEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_ZxrosAMATInterfaceOutAmatEnable_Type.__name__=_C
_ZxrosAMATInterfaceOutAmatEnable_Object=MibTableColumn
zxrosAMATInterfaceOutAmatEnable=_ZxrosAMATInterfaceOutAmatEnable_Object((1,3,6,1,4,1,3902,100,1001,1,1,3),_ZxrosAMATInterfaceOutAmatEnable_Type())
zxrosAMATInterfaceOutAmatEnable.setMaxAccess(_H)
if mibBuilder.loadTexts:zxrosAMATInterfaceOutAmatEnable.setStatus(_A)
_ZxrosAMATInterfaceStatisticTable_Object=MibTable
zxrosAMATInterfaceStatisticTable=_ZxrosAMATInterfaceStatisticTable_Object((1,3,6,1,4,1,3902,100,1001,2))
if mibBuilder.loadTexts:zxrosAMATInterfaceStatisticTable.setStatus(_A)
_ZxrosAMATInterfaceStatisticEntry_Object=MibTableRow
zxrosAMATInterfaceStatisticEntry=_ZxrosAMATInterfaceStatisticEntry_Object((1,3,6,1,4,1,3902,100,1001,2,1))
zxrosAMATInterfaceStatisticEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:zxrosAMATInterfaceStatisticEntry.setStatus(_A)
_ZxrosAMATInterfaceStatisticIfIndex_Type=Integer32
_ZxrosAMATInterfaceStatisticIfIndex_Object=MibTableColumn
zxrosAMATInterfaceStatisticIfIndex=_ZxrosAMATInterfaceStatisticIfIndex_Object((1,3,6,1,4,1,3902,100,1001,2,1,1),_ZxrosAMATInterfaceStatisticIfIndex_Type())
zxrosAMATInterfaceStatisticIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:zxrosAMATInterfaceStatisticIfIndex.setStatus(_A)
_ZxrosAMATInFilterpackets_Type=Counter64
_ZxrosAMATInFilterpackets_Object=MibTableColumn
zxrosAMATInFilterpackets=_ZxrosAMATInFilterpackets_Object((1,3,6,1,4,1,3902,100,1001,2,1,2),_ZxrosAMATInFilterpackets_Type())
zxrosAMATInFilterpackets.setMaxAccess(_B)
if mibBuilder.loadTexts:zxrosAMATInFilterpackets.setStatus(_A)
_ZxrosAMATOutFilterpackets_Type=Counter64
_ZxrosAMATOutFilterpackets_Object=MibTableColumn
zxrosAMATOutFilterpackets=_ZxrosAMATOutFilterpackets_Object((1,3,6,1,4,1,3902,100,1001,2,1,3),_ZxrosAMATOutFilterpackets_Type())
zxrosAMATOutFilterpackets.setMaxAccess(_B)
if mibBuilder.loadTexts:zxrosAMATOutFilterpackets.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'zte':zte,'zxros':zxros,'zxrosAMATIF':zxrosAMATIF,'zxrosAMATInterfaceEnableTable':zxrosAMATInterfaceEnableTable,'zxrosAMATInterfaceEnableEntry':zxrosAMATInterfaceEnableEntry,_E:zxrosAMATInterfaceEnableIfIndex,'zxrosAMATInterfaceInAmatEnable':zxrosAMATInterfaceInAmatEnable,'zxrosAMATInterfaceOutAmatEnable':zxrosAMATInterfaceOutAmatEnable,'zxrosAMATInterfaceStatisticTable':zxrosAMATInterfaceStatisticTable,'zxrosAMATInterfaceStatisticEntry':zxrosAMATInterfaceStatisticEntry,_I:zxrosAMATInterfaceStatisticIfIndex,'zxrosAMATInFilterpackets':zxrosAMATInFilterpackets,'zxrosAMATOutFilterpackets':zxrosAMATOutFilterpackets})