_P='capwapDot11WlanBindGroup'
_O='capwapDot11WlanGroup'
_N='capwapDot11WlanBindRowStatus'
_M='capwapDot11WlanBindBssIfIndex'
_L='capwapDot11WlanBindWlanId'
_K='capwapDot11WlanRowStatus'
_J='capwapDot11WlanTunnelMode'
_I='capwapDot11WlanMacType'
_H='capwapDot11WlanProfileIfIndex'
_G='ifIndex'
_F='IF-MIB'
_E='read-only'
_D='capwapDot11WlanProfileId'
_C='read-create'
_B='CAPWAP-DOT11-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CapwapBaseMacTypeTC,CapwapBaseTunnelModeTC=mibBuilder.importSymbols('CAPWAP-BASE-MIB','CapwapBaseMacTypeTC','CapwapBaseTunnelModeTC')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_F,'InterfaceIndex',_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
capwapDot11MIB=ModuleIdentity((1,3,6,1,2,1,195))
if mibBuilder.loadTexts:capwapDot11MIB.setRevisions(('2010-04-30 00:00',))
class CapwapDot11WlanIdTC(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
class CapwapDot11WlanIdProfileTC(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,512))
_CapwapDot11Objects_ObjectIdentity=ObjectIdentity
capwapDot11Objects=_CapwapDot11Objects_ObjectIdentity((1,3,6,1,2,1,195,1))
_CapwapDot11WlanTable_Object=MibTable
capwapDot11WlanTable=_CapwapDot11WlanTable_Object((1,3,6,1,2,1,195,1,1))
if mibBuilder.loadTexts:capwapDot11WlanTable.setStatus(_A)
_CapwapDot11WlanEntry_Object=MibTableRow
capwapDot11WlanEntry=_CapwapDot11WlanEntry_Object((1,3,6,1,2,1,195,1,1,1))
capwapDot11WlanEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:capwapDot11WlanEntry.setStatus(_A)
_CapwapDot11WlanProfileId_Type=CapwapDot11WlanIdProfileTC
_CapwapDot11WlanProfileId_Object=MibTableColumn
capwapDot11WlanProfileId=_CapwapDot11WlanProfileId_Object((1,3,6,1,2,1,195,1,1,1,1),_CapwapDot11WlanProfileId_Type())
capwapDot11WlanProfileId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:capwapDot11WlanProfileId.setStatus(_A)
_CapwapDot11WlanProfileIfIndex_Type=InterfaceIndex
_CapwapDot11WlanProfileIfIndex_Object=MibTableColumn
capwapDot11WlanProfileIfIndex=_CapwapDot11WlanProfileIfIndex_Object((1,3,6,1,2,1,195,1,1,1,2),_CapwapDot11WlanProfileIfIndex_Type())
capwapDot11WlanProfileIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:capwapDot11WlanProfileIfIndex.setStatus(_A)
_CapwapDot11WlanMacType_Type=CapwapBaseMacTypeTC
_CapwapDot11WlanMacType_Object=MibTableColumn
capwapDot11WlanMacType=_CapwapDot11WlanMacType_Object((1,3,6,1,2,1,195,1,1,1,3),_CapwapDot11WlanMacType_Type())
capwapDot11WlanMacType.setMaxAccess(_C)
if mibBuilder.loadTexts:capwapDot11WlanMacType.setStatus(_A)
_CapwapDot11WlanTunnelMode_Type=CapwapBaseTunnelModeTC
_CapwapDot11WlanTunnelMode_Object=MibTableColumn
capwapDot11WlanTunnelMode=_CapwapDot11WlanTunnelMode_Object((1,3,6,1,2,1,195,1,1,1,4),_CapwapDot11WlanTunnelMode_Type())
capwapDot11WlanTunnelMode.setMaxAccess(_C)
if mibBuilder.loadTexts:capwapDot11WlanTunnelMode.setStatus(_A)
_CapwapDot11WlanRowStatus_Type=RowStatus
_CapwapDot11WlanRowStatus_Object=MibTableColumn
capwapDot11WlanRowStatus=_CapwapDot11WlanRowStatus_Object((1,3,6,1,2,1,195,1,1,1,5),_CapwapDot11WlanRowStatus_Type())
capwapDot11WlanRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:capwapDot11WlanRowStatus.setStatus(_A)
_CapwapDot11WlanBindTable_Object=MibTable
capwapDot11WlanBindTable=_CapwapDot11WlanBindTable_Object((1,3,6,1,2,1,195,1,2))
if mibBuilder.loadTexts:capwapDot11WlanBindTable.setStatus(_A)
_CapwapDot11WlanBindEntry_Object=MibTableRow
capwapDot11WlanBindEntry=_CapwapDot11WlanBindEntry_Object((1,3,6,1,2,1,195,1,2,1))
capwapDot11WlanBindEntry.setIndexNames((0,_F,_G),(0,_B,_D))
if mibBuilder.loadTexts:capwapDot11WlanBindEntry.setStatus(_A)
_CapwapDot11WlanBindWlanId_Type=CapwapDot11WlanIdTC
_CapwapDot11WlanBindWlanId_Object=MibTableColumn
capwapDot11WlanBindWlanId=_CapwapDot11WlanBindWlanId_Object((1,3,6,1,2,1,195,1,2,1,1),_CapwapDot11WlanBindWlanId_Type())
capwapDot11WlanBindWlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:capwapDot11WlanBindWlanId.setStatus(_A)
_CapwapDot11WlanBindBssIfIndex_Type=InterfaceIndex
_CapwapDot11WlanBindBssIfIndex_Object=MibTableColumn
capwapDot11WlanBindBssIfIndex=_CapwapDot11WlanBindBssIfIndex_Object((1,3,6,1,2,1,195,1,2,1,2),_CapwapDot11WlanBindBssIfIndex_Type())
capwapDot11WlanBindBssIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:capwapDot11WlanBindBssIfIndex.setStatus(_A)
_CapwapDot11WlanBindRowStatus_Type=RowStatus
_CapwapDot11WlanBindRowStatus_Object=MibTableColumn
capwapDot11WlanBindRowStatus=_CapwapDot11WlanBindRowStatus_Object((1,3,6,1,2,1,195,1,2,1,3),_CapwapDot11WlanBindRowStatus_Type())
capwapDot11WlanBindRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:capwapDot11WlanBindRowStatus.setStatus(_A)
_CapwapDot11Conformance_ObjectIdentity=ObjectIdentity
capwapDot11Conformance=_CapwapDot11Conformance_ObjectIdentity((1,3,6,1,2,1,195,2))
_CapwapDot11Groups_ObjectIdentity=ObjectIdentity
capwapDot11Groups=_CapwapDot11Groups_ObjectIdentity((1,3,6,1,2,1,195,2,1))
_CapwapDot11Compliances_ObjectIdentity=ObjectIdentity
capwapDot11Compliances=_CapwapDot11Compliances_ObjectIdentity((1,3,6,1,2,1,195,2,2))
capwapDot11WlanGroup=ObjectGroup((1,3,6,1,2,1,195,2,1,1))
capwapDot11WlanGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:capwapDot11WlanGroup.setStatus(_A)
capwapDot11WlanBindGroup=ObjectGroup((1,3,6,1,2,1,195,2,1,2))
capwapDot11WlanBindGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:capwapDot11WlanBindGroup.setStatus(_A)
capwapDot11Compliance=ModuleCompliance((1,3,6,1,2,1,195,2,2,1))
capwapDot11Compliance.setObjects(*((_B,_O),(_B,_P)))
if mibBuilder.loadTexts:capwapDot11Compliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CapwapDot11WlanIdTC':CapwapDot11WlanIdTC,'CapwapDot11WlanIdProfileTC':CapwapDot11WlanIdProfileTC,'capwapDot11MIB':capwapDot11MIB,'capwapDot11Objects':capwapDot11Objects,'capwapDot11WlanTable':capwapDot11WlanTable,'capwapDot11WlanEntry':capwapDot11WlanEntry,_D:capwapDot11WlanProfileId,_H:capwapDot11WlanProfileIfIndex,_I:capwapDot11WlanMacType,_J:capwapDot11WlanTunnelMode,_K:capwapDot11WlanRowStatus,'capwapDot11WlanBindTable':capwapDot11WlanBindTable,'capwapDot11WlanBindEntry':capwapDot11WlanBindEntry,_L:capwapDot11WlanBindWlanId,_M:capwapDot11WlanBindBssIfIndex,_N:capwapDot11WlanBindRowStatus,'capwapDot11Conformance':capwapDot11Conformance,'capwapDot11Groups':capwapDot11Groups,_O:capwapDot11WlanGroup,_P:capwapDot11WlanBindGroup,'capwapDot11Compliances':capwapDot11Compliances,'capwapDot11Compliance':capwapDot11Compliance})