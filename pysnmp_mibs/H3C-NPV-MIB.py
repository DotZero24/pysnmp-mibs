_J='read-only'
_I='read-create'
_H='TruthValue'
_G='Unsigned32'
_F='read-write'
_E='ifIndex'
_D='IF-MIB'
_C='h3cVsanIndex'
_B='H3C-VSAN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
H3cFcVsanIndex,=mibBuilder.importSymbols('H3C-FC-TC-MIB','H3cFcVsanIndex')
h3cSan,h3cVsanIndex=mibBuilder.importSymbols(_B,'h3cSan',_C)
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_D,'InterfaceIndex',_E)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp',_H)
h3cNpv=ModuleIdentity((1,3,6,1,4,1,2011,10,2,127,6))
if mibBuilder.loadTexts:h3cNpv.setRevisions(('2014-07-21 00:00','2013-04-02 00:00'))
class H3cNpvIfIndexList(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,65535))
_H3cNpvMibObjects_ObjectIdentity=ObjectIdentity
h3cNpvMibObjects=_H3cNpvMibObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,127,6,1))
_H3cNpvConfiguration_ObjectIdentity=ObjectIdentity
h3cNpvConfiguration=_H3cNpvConfiguration_ObjectIdentity((1,3,6,1,4,1,2011,10,2,127,6,1,1))
_H3cNpvGlobalObjects_ObjectIdentity=ObjectIdentity
h3cNpvGlobalObjects=_H3cNpvGlobalObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,127,6,1,1,1))
_H3cNpvLoadbalanceVsan_Type=H3cFcVsanIndex
_H3cNpvLoadbalanceVsan_Object=MibScalar
h3cNpvLoadbalanceVsan=_H3cNpvLoadbalanceVsan_Object((1,3,6,1,4,1,2011,10,2,127,6,1,1,1,1),_H3cNpvLoadbalanceVsan_Type())
h3cNpvLoadbalanceVsan.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cNpvLoadbalanceVsan.setStatus(_A)
_H3cNpvTrafficMapConfigTable_Object=MibTable
h3cNpvTrafficMapConfigTable=_H3cNpvTrafficMapConfigTable_Object((1,3,6,1,4,1,2011,10,2,127,6,1,1,2))
if mibBuilder.loadTexts:h3cNpvTrafficMapConfigTable.setStatus(_A)
_H3cNpvTrafficMapConfigEntry_Object=MibTableRow
h3cNpvTrafficMapConfigEntry=_H3cNpvTrafficMapConfigEntry_Object((1,3,6,1,4,1,2011,10,2,127,6,1,1,2,1))
h3cNpvTrafficMapConfigEntry.setIndexNames((0,_D,_E),(0,_B,_C))
if mibBuilder.loadTexts:h3cNpvTrafficMapConfigEntry.setStatus(_A)
_H3cNpvTrafficMapExternalIfIndexList_Type=H3cNpvIfIndexList
_H3cNpvTrafficMapExternalIfIndexList_Object=MibTableColumn
h3cNpvTrafficMapExternalIfIndexList=_H3cNpvTrafficMapExternalIfIndexList_Object((1,3,6,1,4,1,2011,10,2,127,6,1,1,2,1,1),_H3cNpvTrafficMapExternalIfIndexList_Type())
h3cNpvTrafficMapExternalIfIndexList.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cNpvTrafficMapExternalIfIndexList.setStatus(_A)
_H3cNpvTrafficMapLastChange_Type=TimeStamp
_H3cNpvTrafficMapLastChange_Object=MibTableColumn
h3cNpvTrafficMapLastChange=_H3cNpvTrafficMapLastChange_Object((1,3,6,1,4,1,2011,10,2,127,6,1,1,2,1,2),_H3cNpvTrafficMapLastChange_Type())
h3cNpvTrafficMapLastChange.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cNpvTrafficMapLastChange.setStatus(_A)
_H3cNpvTrafficMapRowStatus_Type=RowStatus
_H3cNpvTrafficMapRowStatus_Object=MibTableColumn
h3cNpvTrafficMapRowStatus=_H3cNpvTrafficMapRowStatus_Object((1,3,6,1,4,1,2011,10,2,127,6,1,1,2,1,3),_H3cNpvTrafficMapRowStatus_Type())
h3cNpvTrafficMapRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cNpvTrafficMapRowStatus.setStatus(_A)
_H3cNpvServerIfTable_Object=MibTable
h3cNpvServerIfTable=_H3cNpvServerIfTable_Object((1,3,6,1,4,1,2011,10,2,127,6,1,1,3))
if mibBuilder.loadTexts:h3cNpvServerIfTable.setStatus(_A)
_H3cNpvServerIfEntry_Object=MibTableRow
h3cNpvServerIfEntry=_H3cNpvServerIfEntry_Object((1,3,6,1,4,1,2011,10,2,127,6,1,1,3,1))
h3cNpvServerIfEntry.setIndexNames((0,_D,_E),(0,_B,_C))
if mibBuilder.loadTexts:h3cNpvServerIfEntry.setStatus(_A)
_H3cNpvExternalIfIndex_Type=InterfaceIndex
_H3cNpvExternalIfIndex_Object=MibTableColumn
h3cNpvExternalIfIndex=_H3cNpvExternalIfIndex_Object((1,3,6,1,4,1,2011,10,2,127,6,1,1,3,1,1),_H3cNpvExternalIfIndex_Type())
h3cNpvExternalIfIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cNpvExternalIfIndex.setStatus(_A)
_H3cNpvLoadBalanceTable_Object=MibTable
h3cNpvLoadBalanceTable=_H3cNpvLoadBalanceTable_Object((1,3,6,1,4,1,2011,10,2,127,6,1,1,4))
if mibBuilder.loadTexts:h3cNpvLoadBalanceTable.setStatus(_A)
_H3cNpvLoadBalanceEntry_Object=MibTableRow
h3cNpvLoadBalanceEntry=_H3cNpvLoadBalanceEntry_Object((1,3,6,1,4,1,2011,10,2,127,6,1,1,4,1))
h3cNpvLoadBalanceEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:h3cNpvLoadBalanceEntry.setStatus(_A)
class _H3cNpvAutoLoadBalanceEnable_Type(TruthValue):defaultValue=2
_H3cNpvAutoLoadBalanceEnable_Type.__name__=_H
_H3cNpvAutoLoadBalanceEnable_Object=MibTableColumn
h3cNpvAutoLoadBalanceEnable=_H3cNpvAutoLoadBalanceEnable_Object((1,3,6,1,4,1,2011,10,2,127,6,1,1,4,1,1),_H3cNpvAutoLoadBalanceEnable_Type())
h3cNpvAutoLoadBalanceEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cNpvAutoLoadBalanceEnable.setStatus(_A)
class _H3cNpvAutoLoadBalanceInterval_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_H3cNpvAutoLoadBalanceInterval_Type.__name__=_G
_H3cNpvAutoLoadBalanceInterval_Object=MibTableColumn
h3cNpvAutoLoadBalanceInterval=_H3cNpvAutoLoadBalanceInterval_Object((1,3,6,1,4,1,2011,10,2,127,6,1,1,4,1,2),_H3cNpvAutoLoadBalanceInterval_Type())
h3cNpvAutoLoadBalanceInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cNpvAutoLoadBalanceInterval.setStatus(_A)
if mibBuilder.loadTexts:h3cNpvAutoLoadBalanceInterval.setUnits('seconds')
mibBuilder.exportSymbols('H3C-NPV-MIB',**{'H3cNpvIfIndexList':H3cNpvIfIndexList,'h3cNpv':h3cNpv,'h3cNpvMibObjects':h3cNpvMibObjects,'h3cNpvConfiguration':h3cNpvConfiguration,'h3cNpvGlobalObjects':h3cNpvGlobalObjects,'h3cNpvLoadbalanceVsan':h3cNpvLoadbalanceVsan,'h3cNpvTrafficMapConfigTable':h3cNpvTrafficMapConfigTable,'h3cNpvTrafficMapConfigEntry':h3cNpvTrafficMapConfigEntry,'h3cNpvTrafficMapExternalIfIndexList':h3cNpvTrafficMapExternalIfIndexList,'h3cNpvTrafficMapLastChange':h3cNpvTrafficMapLastChange,'h3cNpvTrafficMapRowStatus':h3cNpvTrafficMapRowStatus,'h3cNpvServerIfTable':h3cNpvServerIfTable,'h3cNpvServerIfEntry':h3cNpvServerIfEntry,'h3cNpvExternalIfIndex':h3cNpvExternalIfIndex,'h3cNpvLoadBalanceTable':h3cNpvLoadBalanceTable,'h3cNpvLoadBalanceEntry':h3cNpvLoadBalanceEntry,'h3cNpvAutoLoadBalanceEnable':h3cNpvAutoLoadBalanceEnable,'h3cNpvAutoLoadBalanceInterval':h3cNpvAutoLoadBalanceInterval})