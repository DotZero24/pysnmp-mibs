_H='zxAnVlanTransOriginalCvlan'
_G='zxAnOnuPortId'
_F='not-accessible'
_E='zxAnPonOnuId'
_D='Integer32'
_C='read-write'
_B='ZXANVLANTRANS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
VlanId,=mibBuilder.importSymbols('ZTE-AN-TC-MIB','VlanId')
zxAnPonMib,=mibBuilder.importSymbols('ZTE-MASTER-MIB','zxAnPonMib')
zxAnVlanTrans=ModuleIdentity((1,3,6,1,4,1,3902,1015,1010,10))
_ZxAnVlanTransRuleTable_Object=MibTable
zxAnVlanTransRuleTable=_ZxAnVlanTransRuleTable_Object((1,3,6,1,4,1,3902,1015,1010,10,1))
if mibBuilder.loadTexts:zxAnVlanTransRuleTable.setStatus(_A)
_ZxAnVlanTransRuleEntry_Object=MibTableRow
zxAnVlanTransRuleEntry=_ZxAnVlanTransRuleEntry_Object((1,3,6,1,4,1,3902,1015,1010,10,1,1))
zxAnVlanTransRuleEntry.setIndexNames((0,_B,_E),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:zxAnVlanTransRuleEntry.setStatus(_A)
_ZxAnPonOnuId_Type=Integer32
_ZxAnPonOnuId_Object=MibTableColumn
zxAnPonOnuId=_ZxAnPonOnuId_Object((1,3,6,1,4,1,3902,1015,1010,10,1,1,1),_ZxAnPonOnuId_Type())
zxAnPonOnuId.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnPonOnuId.setStatus(_A)
_ZxAnOnuPortId_Type=Integer32
_ZxAnOnuPortId_Object=MibTableColumn
zxAnOnuPortId=_ZxAnOnuPortId_Object((1,3,6,1,4,1,3902,1015,1010,10,1,1,2),_ZxAnOnuPortId_Type())
zxAnOnuPortId.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnOnuPortId.setStatus(_A)
_ZxAnVlanTransOriginalCvlan_Type=VlanId
_ZxAnVlanTransOriginalCvlan_Object=MibTableColumn
zxAnVlanTransOriginalCvlan=_ZxAnVlanTransOriginalCvlan_Object((1,3,6,1,4,1,3902,1015,1010,10,1,1,3),_ZxAnVlanTransOriginalCvlan_Type())
zxAnVlanTransOriginalCvlan.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnVlanTransOriginalCvlan.setStatus(_A)
_ZxAnVlanTransNewCvlan_Type=VlanId
_ZxAnVlanTransNewCvlan_Object=MibTableColumn
zxAnVlanTransNewCvlan=_ZxAnVlanTransNewCvlan_Object((1,3,6,1,4,1,3902,1015,1010,10,1,1,4),_ZxAnVlanTransNewCvlan_Type())
zxAnVlanTransNewCvlan.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnVlanTransNewCvlan.setStatus(_A)
class _ZxAnVlanTransBroadcast_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),('enable',1)))
_ZxAnVlanTransBroadcast_Type.__name__=_D
_ZxAnVlanTransBroadcast_Object=MibTableColumn
zxAnVlanTransBroadcast=_ZxAnVlanTransBroadcast_Object((1,3,6,1,4,1,3902,1015,1010,10,1,1,5),_ZxAnVlanTransBroadcast_Type())
zxAnVlanTransBroadcast.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnVlanTransBroadcast.setStatus(_A)
class _ZxAnVlanTransMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('oneToOne',1),('nToOne',2)))
_ZxAnVlanTransMode_Type.__name__=_D
_ZxAnVlanTransMode_Object=MibTableColumn
zxAnVlanTransMode=_ZxAnVlanTransMode_Object((1,3,6,1,4,1,3902,1015,1010,10,1,1,6),_ZxAnVlanTransMode_Type())
zxAnVlanTransMode.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnVlanTransMode.setStatus(_A)
_ZxAnVlanTransEntryStatus_Type=RowStatus
_ZxAnVlanTransEntryStatus_Object=MibTableColumn
zxAnVlanTransEntryStatus=_ZxAnVlanTransEntryStatus_Object((1,3,6,1,4,1,3902,1015,1010,10,1,1,10),_ZxAnVlanTransEntryStatus_Type())
zxAnVlanTransEntryStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnVlanTransEntryStatus.setStatus(_A)
_ZxAnVlanTransGlobalTable_Object=MibTable
zxAnVlanTransGlobalTable=_ZxAnVlanTransGlobalTable_Object((1,3,6,1,4,1,3902,1015,1010,10,2))
if mibBuilder.loadTexts:zxAnVlanTransGlobalTable.setStatus(_A)
_ZxAnVlanTransGlobalEntry_Object=MibTableRow
zxAnVlanTransGlobalEntry=_ZxAnVlanTransGlobalEntry_Object((1,3,6,1,4,1,3902,1015,1010,10,2,1))
zxAnVlanTransGlobalEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:zxAnVlanTransGlobalEntry.setStatus(_A)
_ZxAnVlanTransSvlanBase_Type=VlanId
_ZxAnVlanTransSvlanBase_Object=MibTableColumn
zxAnVlanTransSvlanBase=_ZxAnVlanTransSvlanBase_Object((1,3,6,1,4,1,3902,1015,1010,10,2,1,1),_ZxAnVlanTransSvlanBase_Type())
zxAnVlanTransSvlanBase.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnVlanTransSvlanBase.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'zxAnVlanTrans':zxAnVlanTrans,'zxAnVlanTransRuleTable':zxAnVlanTransRuleTable,'zxAnVlanTransRuleEntry':zxAnVlanTransRuleEntry,_E:zxAnPonOnuId,_G:zxAnOnuPortId,_H:zxAnVlanTransOriginalCvlan,'zxAnVlanTransNewCvlan':zxAnVlanTransNewCvlan,'zxAnVlanTransBroadcast':zxAnVlanTransBroadcast,'zxAnVlanTransMode':zxAnVlanTransMode,'zxAnVlanTransEntryStatus':zxAnVlanTransEntryStatus,'zxAnVlanTransGlobalTable':zxAnVlanTransGlobalTable,'zxAnVlanTransGlobalEntry':zxAnVlanTransGlobalEntry,'zxAnVlanTransSvlanBase':zxAnVlanTransSvlanBase})