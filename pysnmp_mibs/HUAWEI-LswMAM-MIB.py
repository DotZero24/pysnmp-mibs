_M='hwdot1qTpFdbGroupSetAddress'
_L='delete'
_K='not-accessible'
_J='hwdot1qTpFdbSetAddress'
_I='hwdot1qMacSearchVlanID'
_H='hwdot1qMacSearchAddress'
_G='hwdot1qVlanIndex'
_F='HUAWEI-LswVLAN-MIB'
_E='read-only'
_D='read-write'
_C='HUAWEI-LswMAM-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lswCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','lswCommon')
hwdot1qVlanIndex,=mibBuilder.importSymbols(_F,_G)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
hwLswMacPort=ModuleIdentity((1,3,6,1,4,1,2011,2,23,1,3))
if mibBuilder.loadTexts:hwLswMacPort.setRevisions(('2001-06-29 00:00',))
class InterfaceIndex(TextualConvention,Integer32):status=_A;displayHint='d'
class PortList(TextualConvention,OctetString):status=_A
_Hwdot1qMacSearchTable_Object=MibTable
hwdot1qMacSearchTable=_Hwdot1qMacSearchTable_Object((1,3,6,1,4,1,2011,2,23,1,3,1))
if mibBuilder.loadTexts:hwdot1qMacSearchTable.setStatus(_A)
_Hwdot1qMacSearchEntry_Object=MibTableRow
hwdot1qMacSearchEntry=_Hwdot1qMacSearchEntry_Object((1,3,6,1,4,1,2011,2,23,1,3,1,1))
hwdot1qMacSearchEntry.setIndexNames((0,_C,_H),(0,_C,_I))
if mibBuilder.loadTexts:hwdot1qMacSearchEntry.setStatus(_A)
_Hwdot1qMacSearchAddress_Type=MacAddress
_Hwdot1qMacSearchAddress_Object=MibTableColumn
hwdot1qMacSearchAddress=_Hwdot1qMacSearchAddress_Object((1,3,6,1,4,1,2011,2,23,1,3,1,1,1),_Hwdot1qMacSearchAddress_Type())
hwdot1qMacSearchAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:hwdot1qMacSearchAddress.setStatus(_A)
class _Hwdot1qMacSearchVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(1,4096))
_Hwdot1qMacSearchVlanID_Type.__name__=_B
_Hwdot1qMacSearchVlanID_Object=MibTableColumn
hwdot1qMacSearchVlanID=_Hwdot1qMacSearchVlanID_Object((1,3,6,1,4,1,2011,2,23,1,3,1,1,2),_Hwdot1qMacSearchVlanID_Type())
hwdot1qMacSearchVlanID.setMaxAccess(_E)
if mibBuilder.loadTexts:hwdot1qMacSearchVlanID.setStatus(_A)
_Hwdot1qMacSearchPort_Type=InterfaceIndex
_Hwdot1qMacSearchPort_Object=MibTableColumn
hwdot1qMacSearchPort=_Hwdot1qMacSearchPort_Object((1,3,6,1,4,1,2011,2,23,1,3,1,1,3),_Hwdot1qMacSearchPort_Type())
hwdot1qMacSearchPort.setMaxAccess(_E)
if mibBuilder.loadTexts:hwdot1qMacSearchPort.setStatus(_A)
_Hwdot1qMacSearchAgeTime_Type=Integer32
_Hwdot1qMacSearchAgeTime_Object=MibTableColumn
hwdot1qMacSearchAgeTime=_Hwdot1qMacSearchAgeTime_Object((1,3,6,1,4,1,2011,2,23,1,3,1,1,4),_Hwdot1qMacSearchAgeTime_Type())
hwdot1qMacSearchAgeTime.setMaxAccess(_E)
if mibBuilder.loadTexts:hwdot1qMacSearchAgeTime.setStatus(_A)
_Hwdot1qTpFdbSetTable_Object=MibTable
hwdot1qTpFdbSetTable=_Hwdot1qTpFdbSetTable_Object((1,3,6,1,4,1,2011,2,23,1,3,2))
if mibBuilder.loadTexts:hwdot1qTpFdbSetTable.setStatus(_A)
_Hwdot1qTpFdbSetEntry_Object=MibTableRow
hwdot1qTpFdbSetEntry=_Hwdot1qTpFdbSetEntry_Object((1,3,6,1,4,1,2011,2,23,1,3,2,1))
hwdot1qTpFdbSetEntry.setIndexNames((0,_F,_G),(0,_C,_J))
if mibBuilder.loadTexts:hwdot1qTpFdbSetEntry.setStatus(_A)
_Hwdot1qTpFdbSetAddress_Type=MacAddress
_Hwdot1qTpFdbSetAddress_Object=MibTableColumn
hwdot1qTpFdbSetAddress=_Hwdot1qTpFdbSetAddress_Object((1,3,6,1,4,1,2011,2,23,1,3,2,1,1),_Hwdot1qTpFdbSetAddress_Type())
hwdot1qTpFdbSetAddress.setMaxAccess(_K)
if mibBuilder.loadTexts:hwdot1qTpFdbSetAddress.setStatus(_A)
_Hwdot1qTpFdbSetPort_Type=InterfaceIndex
_Hwdot1qTpFdbSetPort_Object=MibTableColumn
hwdot1qTpFdbSetPort=_Hwdot1qTpFdbSetPort_Object((1,3,6,1,4,1,2011,2,23,1,3,2,1,2),_Hwdot1qTpFdbSetPort_Type())
hwdot1qTpFdbSetPort.setMaxAccess(_D)
if mibBuilder.loadTexts:hwdot1qTpFdbSetPort.setStatus(_A)
class _Hwdot1qTpFdbSetStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,6,7,9,11)));namedValues=NamedValues(*(('other',1),('learned',3),('static',6),('dynamic',7),('blackhole',9),('security',11)))
_Hwdot1qTpFdbSetStatus_Type.__name__=_B
_Hwdot1qTpFdbSetStatus_Object=MibTableColumn
hwdot1qTpFdbSetStatus=_Hwdot1qTpFdbSetStatus_Object((1,3,6,1,4,1,2011,2,23,1,3,2,1,3),_Hwdot1qTpFdbSetStatus_Type())
hwdot1qTpFdbSetStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hwdot1qTpFdbSetStatus.setStatus(_A)
class _Hwdot1qTpFdbSetOperate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('add',1),(_L,2)))
_Hwdot1qTpFdbSetOperate_Type.__name__=_B
_Hwdot1qTpFdbSetOperate_Object=MibTableColumn
hwdot1qTpFdbSetOperate=_Hwdot1qTpFdbSetOperate_Object((1,3,6,1,4,1,2011,2,23,1,3,2,1,4),_Hwdot1qTpFdbSetOperate_Type())
hwdot1qTpFdbSetOperate.setMaxAccess(_D)
if mibBuilder.loadTexts:hwdot1qTpFdbSetOperate.setStatus(_A)
_Hwdot1qTpFdbGroupSetTable_Object=MibTable
hwdot1qTpFdbGroupSetTable=_Hwdot1qTpFdbGroupSetTable_Object((1,3,6,1,4,1,2011,2,23,1,3,3))
if mibBuilder.loadTexts:hwdot1qTpFdbGroupSetTable.setStatus(_A)
_Hwdot1qTpFdbGroupSetEntry_Object=MibTableRow
hwdot1qTpFdbGroupSetEntry=_Hwdot1qTpFdbGroupSetEntry_Object((1,3,6,1,4,1,2011,2,23,1,3,3,1))
hwdot1qTpFdbGroupSetEntry.setIndexNames((0,_F,_G),(0,_C,_M))
if mibBuilder.loadTexts:hwdot1qTpFdbGroupSetEntry.setStatus(_A)
_Hwdot1qTpFdbGroupSetAddress_Type=MacAddress
_Hwdot1qTpFdbGroupSetAddress_Object=MibTableColumn
hwdot1qTpFdbGroupSetAddress=_Hwdot1qTpFdbGroupSetAddress_Object((1,3,6,1,4,1,2011,2,23,1,3,3,1,1),_Hwdot1qTpFdbGroupSetAddress_Type())
hwdot1qTpFdbGroupSetAddress.setMaxAccess(_K)
if mibBuilder.loadTexts:hwdot1qTpFdbGroupSetAddress.setStatus(_A)
_Hwdot1qTpFdbGroupSetPort_Type=PortList
_Hwdot1qTpFdbGroupSetPort_Object=MibTableColumn
hwdot1qTpFdbGroupSetPort=_Hwdot1qTpFdbGroupSetPort_Object((1,3,6,1,4,1,2011,2,23,1,3,3,1,2),_Hwdot1qTpFdbGroupSetPort_Type())
hwdot1qTpFdbGroupSetPort.setMaxAccess(_D)
if mibBuilder.loadTexts:hwdot1qTpFdbGroupSetPort.setStatus(_A)
class _Hwdot1qTpFdbGroupSetOperate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('add',1),(_L,2)))
_Hwdot1qTpFdbGroupSetOperate_Type.__name__=_B
_Hwdot1qTpFdbGroupSetOperate_Object=MibTableColumn
hwdot1qTpFdbGroupSetOperate=_Hwdot1qTpFdbGroupSetOperate_Object((1,3,6,1,4,1,2011,2,23,1,3,3,1,3),_Hwdot1qTpFdbGroupSetOperate_Type())
hwdot1qTpFdbGroupSetOperate.setMaxAccess(_D)
if mibBuilder.loadTexts:hwdot1qTpFdbGroupSetOperate.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'InterfaceIndex':InterfaceIndex,'PortList':PortList,'hwLswMacPort':hwLswMacPort,'hwdot1qMacSearchTable':hwdot1qMacSearchTable,'hwdot1qMacSearchEntry':hwdot1qMacSearchEntry,_H:hwdot1qMacSearchAddress,_I:hwdot1qMacSearchVlanID,'hwdot1qMacSearchPort':hwdot1qMacSearchPort,'hwdot1qMacSearchAgeTime':hwdot1qMacSearchAgeTime,'hwdot1qTpFdbSetTable':hwdot1qTpFdbSetTable,'hwdot1qTpFdbSetEntry':hwdot1qTpFdbSetEntry,_J:hwdot1qTpFdbSetAddress,'hwdot1qTpFdbSetPort':hwdot1qTpFdbSetPort,'hwdot1qTpFdbSetStatus':hwdot1qTpFdbSetStatus,'hwdot1qTpFdbSetOperate':hwdot1qTpFdbSetOperate,'hwdot1qTpFdbGroupSetTable':hwdot1qTpFdbGroupSetTable,'hwdot1qTpFdbGroupSetEntry':hwdot1qTpFdbGroupSetEntry,_M:hwdot1qTpFdbGroupSetAddress,'hwdot1qTpFdbGroupSetPort':hwdot1qTpFdbGroupSetPort,'hwdot1qTpFdbGroupSetOperate':hwdot1qTpFdbGroupSetOperate})