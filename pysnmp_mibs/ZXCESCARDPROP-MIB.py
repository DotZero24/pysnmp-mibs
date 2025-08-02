_E='zxCesCardIndex'
_D='ZXCESCARDPROP-MIB'
_C='InetAddressType'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress',_C)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
zxPwCETH,=mibBuilder.importSymbols('ZTE-MASTER-MIB','zxPwCETH')
zxCesCardPropMIB=ModuleIdentity((1,3,6,1,4,1,3902,1015,1013,3,1,1))
_ZxCesCardPropTable_Object=MibTable
zxCesCardPropTable=_ZxCesCardPropTable_Object((1,3,6,1,4,1,3902,1015,1013,3,1,1,1))
if mibBuilder.loadTexts:zxCesCardPropTable.setStatus(_A)
_ZxCesCardPropEntry_Object=MibTableRow
zxCesCardPropEntry=_ZxCesCardPropEntry_Object((1,3,6,1,4,1,3902,1015,1013,3,1,1,1,1))
zxCesCardPropEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:zxCesCardPropEntry.setStatus(_A)
_ZxCesCardIndex_Type=InterfaceIndex
_ZxCesCardIndex_Object=MibTableColumn
zxCesCardIndex=_ZxCesCardIndex_Object((1,3,6,1,4,1,3902,1015,1013,3,1,1,1,1,1),_ZxCesCardIndex_Type())
zxCesCardIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:zxCesCardIndex.setStatus(_A)
_ZxCesCardPhysAddress_Type=PhysAddress
_ZxCesCardPhysAddress_Object=MibTableColumn
zxCesCardPhysAddress=_ZxCesCardPhysAddress_Object((1,3,6,1,4,1,3902,1015,1013,3,1,1,1,1,2),_ZxCesCardPhysAddress_Type())
zxCesCardPhysAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:zxCesCardPhysAddress.setStatus(_A)
class _ZxCesCardAddrType_Type(InetAddressType):defaultValue=1
_ZxCesCardAddrType_Type.__name__=_C
_ZxCesCardAddrType_Object=MibTableColumn
zxCesCardAddrType=_ZxCesCardAddrType_Object((1,3,6,1,4,1,3902,1015,1013,3,1,1,1,1,3),_ZxCesCardAddrType_Type())
zxCesCardAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxCesCardAddrType.setStatus(_A)
_ZxCesCardAddress_Type=InetAddress
_ZxCesCardAddress_Object=MibTableColumn
zxCesCardAddress=_ZxCesCardAddress_Object((1,3,6,1,4,1,3902,1015,1013,3,1,1,1,1,4),_ZxCesCardAddress_Type())
zxCesCardAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:zxCesCardAddress.setStatus(_A)
_ZxCesCardCfgInfoSend_Type=TruthValue
_ZxCesCardCfgInfoSend_Object=MibTableColumn
zxCesCardCfgInfoSend=_ZxCesCardCfgInfoSend_Object((1,3,6,1,4,1,3902,1015,1013,3,1,1,1,1,5),_ZxCesCardCfgInfoSend_Type())
zxCesCardCfgInfoSend.setMaxAccess(_B)
if mibBuilder.loadTexts:zxCesCardCfgInfoSend.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'zxCesCardPropMIB':zxCesCardPropMIB,'zxCesCardPropTable':zxCesCardPropTable,'zxCesCardPropEntry':zxCesCardPropEntry,_E:zxCesCardIndex,'zxCesCardPhysAddress':zxCesCardPhysAddress,'zxCesCardAddrType':zxCesCardAddrType,'zxCesCardAddress':zxCesCardAddress,'zxCesCardCfgInfoSend':zxCesCardCfgInfoSend})