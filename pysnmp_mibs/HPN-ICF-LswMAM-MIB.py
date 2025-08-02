_M='hpnicfdot1qTpFdbGroupSetAddress'
_L='delete'
_K='not-accessible'
_J='hpnicfdot1qTpFdbSetAddress'
_I='hpnicfdot1qMacSearchVlanID'
_H='hpnicfdot1qMacSearchAddress'
_G='hpnicfdot1qVlanIndex'
_F='HPN-ICF-LswVLAN-MIB'
_E='read-only'
_D='read-write'
_C='HPN-ICF-LswMAM-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfdot1qVlanIndex,=mibBuilder.importSymbols(_F,_G)
hpnicflswCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicflswCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
hpnicfLswMacPort=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,8,35,3))
if mibBuilder.loadTexts:hpnicfLswMacPort.setRevisions(('2001-06-29 00:00',))
class InterfaceIndex(TextualConvention,Integer32):status=_A;displayHint='d'
class PortList(TextualConvention,OctetString):status=_A
_Hpnicfdot1qMacSearchTable_Object=MibTable
hpnicfdot1qMacSearchTable=_Hpnicfdot1qMacSearchTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,3,1))
if mibBuilder.loadTexts:hpnicfdot1qMacSearchTable.setStatus(_A)
_Hpnicfdot1qMacSearchEntry_Object=MibTableRow
hpnicfdot1qMacSearchEntry=_Hpnicfdot1qMacSearchEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,3,1,1))
hpnicfdot1qMacSearchEntry.setIndexNames((0,_C,_H),(0,_C,_I))
if mibBuilder.loadTexts:hpnicfdot1qMacSearchEntry.setStatus(_A)
_Hpnicfdot1qMacSearchAddress_Type=MacAddress
_Hpnicfdot1qMacSearchAddress_Object=MibTableColumn
hpnicfdot1qMacSearchAddress=_Hpnicfdot1qMacSearchAddress_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,3,1,1,1),_Hpnicfdot1qMacSearchAddress_Type())
hpnicfdot1qMacSearchAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfdot1qMacSearchAddress.setStatus(_A)
class _Hpnicfdot1qMacSearchVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(1,4096))
_Hpnicfdot1qMacSearchVlanID_Type.__name__=_B
_Hpnicfdot1qMacSearchVlanID_Object=MibTableColumn
hpnicfdot1qMacSearchVlanID=_Hpnicfdot1qMacSearchVlanID_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,3,1,1,2),_Hpnicfdot1qMacSearchVlanID_Type())
hpnicfdot1qMacSearchVlanID.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfdot1qMacSearchVlanID.setStatus(_A)
_Hpnicfdot1qMacSearchPort_Type=InterfaceIndex
_Hpnicfdot1qMacSearchPort_Object=MibTableColumn
hpnicfdot1qMacSearchPort=_Hpnicfdot1qMacSearchPort_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,3,1,1,3),_Hpnicfdot1qMacSearchPort_Type())
hpnicfdot1qMacSearchPort.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfdot1qMacSearchPort.setStatus(_A)
_Hpnicfdot1qMacSearchAgeTime_Type=Integer32
_Hpnicfdot1qMacSearchAgeTime_Object=MibTableColumn
hpnicfdot1qMacSearchAgeTime=_Hpnicfdot1qMacSearchAgeTime_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,3,1,1,4),_Hpnicfdot1qMacSearchAgeTime_Type())
hpnicfdot1qMacSearchAgeTime.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfdot1qMacSearchAgeTime.setStatus(_A)
_Hpnicfdot1qTpFdbSetTable_Object=MibTable
hpnicfdot1qTpFdbSetTable=_Hpnicfdot1qTpFdbSetTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,3,2))
if mibBuilder.loadTexts:hpnicfdot1qTpFdbSetTable.setStatus(_A)
_Hpnicfdot1qTpFdbSetEntry_Object=MibTableRow
hpnicfdot1qTpFdbSetEntry=_Hpnicfdot1qTpFdbSetEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,3,2,1))
hpnicfdot1qTpFdbSetEntry.setIndexNames((0,_F,_G),(0,_C,_J))
if mibBuilder.loadTexts:hpnicfdot1qTpFdbSetEntry.setStatus(_A)
_Hpnicfdot1qTpFdbSetAddress_Type=MacAddress
_Hpnicfdot1qTpFdbSetAddress_Object=MibTableColumn
hpnicfdot1qTpFdbSetAddress=_Hpnicfdot1qTpFdbSetAddress_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,3,2,1,1),_Hpnicfdot1qTpFdbSetAddress_Type())
hpnicfdot1qTpFdbSetAddress.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfdot1qTpFdbSetAddress.setStatus(_A)
_Hpnicfdot1qTpFdbSetPort_Type=InterfaceIndex
_Hpnicfdot1qTpFdbSetPort_Object=MibTableColumn
hpnicfdot1qTpFdbSetPort=_Hpnicfdot1qTpFdbSetPort_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,3,2,1,2),_Hpnicfdot1qTpFdbSetPort_Type())
hpnicfdot1qTpFdbSetPort.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdot1qTpFdbSetPort.setStatus(_A)
class _Hpnicfdot1qTpFdbSetStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,6,7,9,11)));namedValues=NamedValues(*(('other',1),('learned',3),('static',6),('dynamic',7),('blackhole',9),('security',11)))
_Hpnicfdot1qTpFdbSetStatus_Type.__name__=_B
_Hpnicfdot1qTpFdbSetStatus_Object=MibTableColumn
hpnicfdot1qTpFdbSetStatus=_Hpnicfdot1qTpFdbSetStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,3,2,1,3),_Hpnicfdot1qTpFdbSetStatus_Type())
hpnicfdot1qTpFdbSetStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdot1qTpFdbSetStatus.setStatus(_A)
class _Hpnicfdot1qTpFdbSetOperate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('add',1),(_L,2)))
_Hpnicfdot1qTpFdbSetOperate_Type.__name__=_B
_Hpnicfdot1qTpFdbSetOperate_Object=MibTableColumn
hpnicfdot1qTpFdbSetOperate=_Hpnicfdot1qTpFdbSetOperate_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,3,2,1,4),_Hpnicfdot1qTpFdbSetOperate_Type())
hpnicfdot1qTpFdbSetOperate.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdot1qTpFdbSetOperate.setStatus(_A)
_Hpnicfdot1qTpFdbGroupSetTable_Object=MibTable
hpnicfdot1qTpFdbGroupSetTable=_Hpnicfdot1qTpFdbGroupSetTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,3,3))
if mibBuilder.loadTexts:hpnicfdot1qTpFdbGroupSetTable.setStatus(_A)
_Hpnicfdot1qTpFdbGroupSetEntry_Object=MibTableRow
hpnicfdot1qTpFdbGroupSetEntry=_Hpnicfdot1qTpFdbGroupSetEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,3,3,1))
hpnicfdot1qTpFdbGroupSetEntry.setIndexNames((0,_F,_G),(0,_C,_M))
if mibBuilder.loadTexts:hpnicfdot1qTpFdbGroupSetEntry.setStatus(_A)
_Hpnicfdot1qTpFdbGroupSetAddress_Type=MacAddress
_Hpnicfdot1qTpFdbGroupSetAddress_Object=MibTableColumn
hpnicfdot1qTpFdbGroupSetAddress=_Hpnicfdot1qTpFdbGroupSetAddress_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,3,3,1,1),_Hpnicfdot1qTpFdbGroupSetAddress_Type())
hpnicfdot1qTpFdbGroupSetAddress.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfdot1qTpFdbGroupSetAddress.setStatus(_A)
_Hpnicfdot1qTpFdbGroupSetPort_Type=PortList
_Hpnicfdot1qTpFdbGroupSetPort_Object=MibTableColumn
hpnicfdot1qTpFdbGroupSetPort=_Hpnicfdot1qTpFdbGroupSetPort_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,3,3,1,2),_Hpnicfdot1qTpFdbGroupSetPort_Type())
hpnicfdot1qTpFdbGroupSetPort.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdot1qTpFdbGroupSetPort.setStatus(_A)
class _Hpnicfdot1qTpFdbGroupSetOperate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('add',1),(_L,2)))
_Hpnicfdot1qTpFdbGroupSetOperate_Type.__name__=_B
_Hpnicfdot1qTpFdbGroupSetOperate_Object=MibTableColumn
hpnicfdot1qTpFdbGroupSetOperate=_Hpnicfdot1qTpFdbGroupSetOperate_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,3,3,1,3),_Hpnicfdot1qTpFdbGroupSetOperate_Type())
hpnicfdot1qTpFdbGroupSetOperate.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdot1qTpFdbGroupSetOperate.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'InterfaceIndex':InterfaceIndex,'PortList':PortList,'hpnicfLswMacPort':hpnicfLswMacPort,'hpnicfdot1qMacSearchTable':hpnicfdot1qMacSearchTable,'hpnicfdot1qMacSearchEntry':hpnicfdot1qMacSearchEntry,_H:hpnicfdot1qMacSearchAddress,_I:hpnicfdot1qMacSearchVlanID,'hpnicfdot1qMacSearchPort':hpnicfdot1qMacSearchPort,'hpnicfdot1qMacSearchAgeTime':hpnicfdot1qMacSearchAgeTime,'hpnicfdot1qTpFdbSetTable':hpnicfdot1qTpFdbSetTable,'hpnicfdot1qTpFdbSetEntry':hpnicfdot1qTpFdbSetEntry,_J:hpnicfdot1qTpFdbSetAddress,'hpnicfdot1qTpFdbSetPort':hpnicfdot1qTpFdbSetPort,'hpnicfdot1qTpFdbSetStatus':hpnicfdot1qTpFdbSetStatus,'hpnicfdot1qTpFdbSetOperate':hpnicfdot1qTpFdbSetOperate,'hpnicfdot1qTpFdbGroupSetTable':hpnicfdot1qTpFdbGroupSetTable,'hpnicfdot1qTpFdbGroupSetEntry':hpnicfdot1qTpFdbGroupSetEntry,_M:hpnicfdot1qTpFdbGroupSetAddress,'hpnicfdot1qTpFdbGroupSetPort':hpnicfdot1qTpFdbGroupSetPort,'hpnicfdot1qTpFdbGroupSetOperate':hpnicfdot1qTpFdbGroupSetOperate})