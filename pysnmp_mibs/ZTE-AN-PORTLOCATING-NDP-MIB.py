_O='zxAnPortLocatingNdpLogicalId'
_N='zxAnPortLocatingNdpIfType'
_M='zxAnPortLocatingNdpOnu'
_L='zxAnPortLocatingNdpPort'
_K='zxAnPortLocatingNdpSlot'
_J='zxAnPortLocatingNdpShelf'
_I='zxAnPortLocatingNdpRack'
_H='disable'
_G='enable'
_F='TruthValue'
_E='read-write'
_D='Integer32'
_C='not-accessible'
_B='ZTE-AN-PORTLOCATING-NDP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_F)
zxAnPortLocatingMib,=mibBuilder.importSymbols('ZTE-AN-PORT-LOCATING-MIB','zxAnPortLocatingMib')
zxAn,=mibBuilder.importSymbols('ZTE-AN-TC-MIB','zxAn')
zxAnPortLocatingNdpMib=ModuleIdentity((1,3,6,1,4,1,3902,1015,32,45))
_ZxAnPortLocatingNdpGlobal_ObjectIdentity=ObjectIdentity
zxAnPortLocatingNdpGlobal=_ZxAnPortLocatingNdpGlobal_ObjectIdentity((1,3,6,1,4,1,3902,1015,32,45,1))
class _ZxAnNdpLioEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_ZxAnNdpLioEnable_Type.__name__=_D
_ZxAnNdpLioEnable_Object=MibScalar
zxAnNdpLioEnable=_ZxAnNdpLioEnable_Object((1,3,6,1,4,1,3902,1015,32,45,1,1),_ZxAnNdpLioEnable_Type())
zxAnNdpLioEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnNdpLioEnable.setStatus(_A)
_ZxAnPortLocatingNdpTable_Object=MibTable
zxAnPortLocatingNdpTable=_ZxAnPortLocatingNdpTable_Object((1,3,6,1,4,1,3902,1015,32,45,2))
if mibBuilder.loadTexts:zxAnPortLocatingNdpTable.setStatus(_A)
_ZxAnPortLocatingNdpEntry_Object=MibTableRow
zxAnPortLocatingNdpEntry=_ZxAnPortLocatingNdpEntry_Object((1,3,6,1,4,1,3902,1015,32,45,2,1))
zxAnPortLocatingNdpEntry.setIndexNames((0,_B,_I),(0,_B,_J),(0,_B,_K),(0,_B,_L),(0,_B,_M),(0,_B,_N),(0,_B,_O))
if mibBuilder.loadTexts:zxAnPortLocatingNdpEntry.setStatus(_A)
_ZxAnPortLocatingNdpRack_Type=Integer32
_ZxAnPortLocatingNdpRack_Object=MibTableColumn
zxAnPortLocatingNdpRack=_ZxAnPortLocatingNdpRack_Object((1,3,6,1,4,1,3902,1015,32,45,2,1,1),_ZxAnPortLocatingNdpRack_Type())
zxAnPortLocatingNdpRack.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnPortLocatingNdpRack.setStatus(_A)
_ZxAnPortLocatingNdpShelf_Type=Integer32
_ZxAnPortLocatingNdpShelf_Object=MibTableColumn
zxAnPortLocatingNdpShelf=_ZxAnPortLocatingNdpShelf_Object((1,3,6,1,4,1,3902,1015,32,45,2,1,2),_ZxAnPortLocatingNdpShelf_Type())
zxAnPortLocatingNdpShelf.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnPortLocatingNdpShelf.setStatus(_A)
_ZxAnPortLocatingNdpSlot_Type=Integer32
_ZxAnPortLocatingNdpSlot_Object=MibTableColumn
zxAnPortLocatingNdpSlot=_ZxAnPortLocatingNdpSlot_Object((1,3,6,1,4,1,3902,1015,32,45,2,1,3),_ZxAnPortLocatingNdpSlot_Type())
zxAnPortLocatingNdpSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnPortLocatingNdpSlot.setStatus(_A)
_ZxAnPortLocatingNdpPort_Type=Integer32
_ZxAnPortLocatingNdpPort_Object=MibTableColumn
zxAnPortLocatingNdpPort=_ZxAnPortLocatingNdpPort_Object((1,3,6,1,4,1,3902,1015,32,45,2,1,4),_ZxAnPortLocatingNdpPort_Type())
zxAnPortLocatingNdpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnPortLocatingNdpPort.setStatus(_A)
_ZxAnPortLocatingNdpOnu_Type=Integer32
_ZxAnPortLocatingNdpOnu_Object=MibTableColumn
zxAnPortLocatingNdpOnu=_ZxAnPortLocatingNdpOnu_Object((1,3,6,1,4,1,3902,1015,32,45,2,1,5),_ZxAnPortLocatingNdpOnu_Type())
zxAnPortLocatingNdpOnu.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnPortLocatingNdpOnu.setStatus(_A)
class _ZxAnPortLocatingNdpIfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,4)));namedValues=NamedValues(*(('bridgePort',2),('ponVPort',4)))
_ZxAnPortLocatingNdpIfType_Type.__name__=_D
_ZxAnPortLocatingNdpIfType_Object=MibTableColumn
zxAnPortLocatingNdpIfType=_ZxAnPortLocatingNdpIfType_Object((1,3,6,1,4,1,3902,1015,32,45,2,1,6),_ZxAnPortLocatingNdpIfType_Type())
zxAnPortLocatingNdpIfType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnPortLocatingNdpIfType.setStatus(_A)
_ZxAnPortLocatingNdpLogicalId_Type=ObjectIdentifier
_ZxAnPortLocatingNdpLogicalId_Object=MibTableColumn
zxAnPortLocatingNdpLogicalId=_ZxAnPortLocatingNdpLogicalId_Object((1,3,6,1,4,1,3902,1015,32,45,2,1,7),_ZxAnPortLocatingNdpLogicalId_Type())
zxAnPortLocatingNdpLogicalId.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnPortLocatingNdpLogicalId.setStatus(_A)
class _ZxAnNdpLioIfConfEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_ZxAnNdpLioIfConfEnable_Type.__name__=_D
_ZxAnNdpLioIfConfEnable_Object=MibTableColumn
zxAnNdpLioIfConfEnable=_ZxAnNdpLioIfConfEnable_Object((1,3,6,1,4,1,3902,1015,32,45,2,1,8),_ZxAnNdpLioIfConfEnable_Type())
zxAnNdpLioIfConfEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnNdpLioIfConfEnable.setStatus(_A)
class _ZxAnNdpLioIfConfTrust_Type(TruthValue):defaultValue=2
_ZxAnNdpLioIfConfTrust_Type.__name__=_F
_ZxAnNdpLioIfConfTrust_Object=MibTableColumn
zxAnNdpLioIfConfTrust=_ZxAnNdpLioIfConfTrust_Object((1,3,6,1,4,1,3902,1015,32,45,2,1,9),_ZxAnNdpLioIfConfTrust_Type())
zxAnNdpLioIfConfTrust.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnNdpLioIfConfTrust.setStatus(_A)
class _ZxAnNdpLioIfConfPolicy_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('keep',1),('replace',2),('discard',3),('add',4)))
_ZxAnNdpLioIfConfPolicy_Type.__name__=_D
_ZxAnNdpLioIfConfPolicy_Object=MibTableColumn
zxAnNdpLioIfConfPolicy=_ZxAnNdpLioIfConfPolicy_Object((1,3,6,1,4,1,3902,1015,32,45,2,1,10),_ZxAnNdpLioIfConfPolicy_Type())
zxAnNdpLioIfConfPolicy.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnNdpLioIfConfPolicy.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'zxAnPortLocatingNdpMib':zxAnPortLocatingNdpMib,'zxAnPortLocatingNdpGlobal':zxAnPortLocatingNdpGlobal,'zxAnNdpLioEnable':zxAnNdpLioEnable,'zxAnPortLocatingNdpTable':zxAnPortLocatingNdpTable,'zxAnPortLocatingNdpEntry':zxAnPortLocatingNdpEntry,_I:zxAnPortLocatingNdpRack,_J:zxAnPortLocatingNdpShelf,_K:zxAnPortLocatingNdpSlot,_L:zxAnPortLocatingNdpPort,_M:zxAnPortLocatingNdpOnu,_N:zxAnPortLocatingNdpIfType,_O:zxAnPortLocatingNdpLogicalId,'zxAnNdpLioIfConfEnable':zxAnNdpLioIfConfEnable,'zxAnNdpLioIfConfTrust':zxAnNdpLioIfConfTrust,'zxAnNdpLioIfConfPolicy':zxAnNdpLioIfConfPolicy})