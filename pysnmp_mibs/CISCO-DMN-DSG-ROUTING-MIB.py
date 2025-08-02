_I='unicastRoutesIndex'
_H='staticRouteIndex'
_G='multicastRouteIndex'
_F='yes'
_E='CISCO-DMN-DSG-ROUTING-MIB'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoDSGUtilities,=mibBuilder.importSymbols('CISCO-DMN-DSG-ROOT-MIB','ciscoDSGUtilities')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
ciscoDSGRouting=ModuleIdentity((1,3,6,1,4,1,1429,2,2,5,40))
if mibBuilder.loadTexts:ciscoDSGRouting.setRevisions(('2012-05-14 15:00','2012-03-07 07:30'))
_MulticastRouteTable_Object=MibTable
multicastRouteTable=_MulticastRouteTable_Object((1,3,6,1,4,1,1429,2,2,5,40,1))
if mibBuilder.loadTexts:multicastRouteTable.setStatus(_A)
_MulticastRouteEntry_Object=MibTableRow
multicastRouteEntry=_MulticastRouteEntry_Object((1,3,6,1,4,1,1429,2,2,5,40,1,1))
multicastRouteEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:multicastRouteEntry.setStatus(_A)
class _MulticastRouteIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_MulticastRouteIndex_Type.__name__=_B
_MulticastRouteIndex_Object=MibTableColumn
multicastRouteIndex=_MulticastRouteIndex_Object((1,3,6,1,4,1,1429,2,2,5,40,1,1,1),_MulticastRouteIndex_Type())
multicastRouteIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:multicastRouteIndex.setStatus(_A)
_MulticastRouteV4IPAddr_Type=IpAddress
_MulticastRouteV4IPAddr_Object=MibTableColumn
multicastRouteV4IPAddr=_MulticastRouteV4IPAddr_Object((1,3,6,1,4,1,1429,2,2,5,40,1,1,2),_MulticastRouteV4IPAddr_Type())
multicastRouteV4IPAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:multicastRouteV4IPAddr.setStatus(_A)
_MulticastRouteRowStatus_Type=RowStatus
_MulticastRouteRowStatus_Object=MibTableColumn
multicastRouteRowStatus=_MulticastRouteRowStatus_Object((1,3,6,1,4,1,1429,2,2,5,40,1,1,3),_MulticastRouteRowStatus_Type())
multicastRouteRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:multicastRouteRowStatus.setStatus(_A)
_StaticRouteTable_Object=MibTable
staticRouteTable=_StaticRouteTable_Object((1,3,6,1,4,1,1429,2,2,5,40,2))
if mibBuilder.loadTexts:staticRouteTable.setStatus(_A)
_StaticRouteEntry_Object=MibTableRow
staticRouteEntry=_StaticRouteEntry_Object((1,3,6,1,4,1,1429,2,2,5,40,2,1))
staticRouteEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:staticRouteEntry.setStatus(_A)
class _StaticRouteIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_StaticRouteIndex_Type.__name__=_B
_StaticRouteIndex_Object=MibTableColumn
staticRouteIndex=_StaticRouteIndex_Object((1,3,6,1,4,1,1429,2,2,5,40,2,1,1),_StaticRouteIndex_Type())
staticRouteIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:staticRouteIndex.setStatus(_A)
_StaticRouteV4IPAddr_Type=IpAddress
_StaticRouteV4IPAddr_Object=MibTableColumn
staticRouteV4IPAddr=_StaticRouteV4IPAddr_Object((1,3,6,1,4,1,1429,2,2,5,40,2,1,2),_StaticRouteV4IPAddr_Type())
staticRouteV4IPAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:staticRouteV4IPAddr.setStatus(_A)
class _StaticRouteV4Mask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,30))
_StaticRouteV4Mask_Type.__name__=_B
_StaticRouteV4Mask_Object=MibTableColumn
staticRouteV4Mask=_StaticRouteV4Mask_Object((1,3,6,1,4,1,1429,2,2,5,40,2,1,3),_StaticRouteV4Mask_Type())
staticRouteV4Mask.setMaxAccess(_D)
if mibBuilder.loadTexts:staticRouteV4Mask.setStatus(_A)
_StaticRouteV4Gateway_Type=IpAddress
_StaticRouteV4Gateway_Object=MibTableColumn
staticRouteV4Gateway=_StaticRouteV4Gateway_Object((1,3,6,1,4,1,1429,2,2,5,40,2,1,4),_StaticRouteV4Gateway_Type())
staticRouteV4Gateway.setMaxAccess(_D)
if mibBuilder.loadTexts:staticRouteV4Gateway.setStatus(_A)
class _StaticRoutePort1Enable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('no',1),(_F,2)))
_StaticRoutePort1Enable_Type.__name__=_B
_StaticRoutePort1Enable_Object=MibTableColumn
staticRoutePort1Enable=_StaticRoutePort1Enable_Object((1,3,6,1,4,1,1429,2,2,5,40,2,1,5),_StaticRoutePort1Enable_Type())
staticRoutePort1Enable.setMaxAccess(_D)
if mibBuilder.loadTexts:staticRoutePort1Enable.setStatus(_A)
class _StaticRoutePort2Enable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('no',1),(_F,2)))
_StaticRoutePort2Enable_Type.__name__=_B
_StaticRoutePort2Enable_Object=MibTableColumn
staticRoutePort2Enable=_StaticRoutePort2Enable_Object((1,3,6,1,4,1,1429,2,2,5,40,2,1,6),_StaticRoutePort2Enable_Type())
staticRoutePort2Enable.setMaxAccess(_D)
if mibBuilder.loadTexts:staticRoutePort2Enable.setStatus(_A)
class _StaticRoutePort3Enable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('no',1),(_F,2)))
_StaticRoutePort3Enable_Type.__name__=_B
_StaticRoutePort3Enable_Object=MibTableColumn
staticRoutePort3Enable=_StaticRoutePort3Enable_Object((1,3,6,1,4,1,1429,2,2,5,40,2,1,7),_StaticRoutePort3Enable_Type())
staticRoutePort3Enable.setMaxAccess(_D)
if mibBuilder.loadTexts:staticRoutePort3Enable.setStatus(_A)
_StaticRouteRowStatus_Type=RowStatus
_StaticRouteRowStatus_Object=MibTableColumn
staticRouteRowStatus=_StaticRouteRowStatus_Object((1,3,6,1,4,1,1429,2,2,5,40,2,1,8),_StaticRouteRowStatus_Type())
staticRouteRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:staticRouteRowStatus.setStatus(_A)
_UnicastRoutesTable_Object=MibTable
unicastRoutesTable=_UnicastRoutesTable_Object((1,3,6,1,4,1,1429,2,2,5,40,3))
if mibBuilder.loadTexts:unicastRoutesTable.setStatus(_A)
_UnicastRoutesEntry_Object=MibTableRow
unicastRoutesEntry=_UnicastRoutesEntry_Object((1,3,6,1,4,1,1429,2,2,5,40,3,1))
unicastRoutesEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:unicastRoutesEntry.setStatus(_A)
class _UnicastRoutesIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_UnicastRoutesIndex_Type.__name__=_B
_UnicastRoutesIndex_Object=MibTableColumn
unicastRoutesIndex=_UnicastRoutesIndex_Object((1,3,6,1,4,1,1429,2,2,5,40,3,1,1),_UnicastRoutesIndex_Type())
unicastRoutesIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:unicastRoutesIndex.setStatus(_A)
class _UnicastRoutesPortID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_UnicastRoutesPortID_Type.__name__=_B
_UnicastRoutesPortID_Object=MibTableColumn
unicastRoutesPortID=_UnicastRoutesPortID_Object((1,3,6,1,4,1,1429,2,2,5,40,3,1,2),_UnicastRoutesPortID_Type())
unicastRoutesPortID.setMaxAccess(_C)
if mibBuilder.loadTexts:unicastRoutesPortID.setStatus(_A)
_UnicastRoutesV4IPAddr_Type=IpAddress
_UnicastRoutesV4IPAddr_Object=MibTableColumn
unicastRoutesV4IPAddr=_UnicastRoutesV4IPAddr_Object((1,3,6,1,4,1,1429,2,2,5,40,3,1,3),_UnicastRoutesV4IPAddr_Type())
unicastRoutesV4IPAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:unicastRoutesV4IPAddr.setStatus(_A)
class _UnicastRoutesV4Mask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_UnicastRoutesV4Mask_Type.__name__=_B
_UnicastRoutesV4Mask_Object=MibTableColumn
unicastRoutesV4Mask=_UnicastRoutesV4Mask_Object((1,3,6,1,4,1,1429,2,2,5,40,3,1,4),_UnicastRoutesV4Mask_Type())
unicastRoutesV4Mask.setMaxAccess(_C)
if mibBuilder.loadTexts:unicastRoutesV4Mask.setStatus(_A)
_UnicastRoutesV4Gateway_Type=IpAddress
_UnicastRoutesV4Gateway_Object=MibTableColumn
unicastRoutesV4Gateway=_UnicastRoutesV4Gateway_Object((1,3,6,1,4,1,1429,2,2,5,40,3,1,5),_UnicastRoutesV4Gateway_Type())
unicastRoutesV4Gateway.setMaxAccess(_C)
if mibBuilder.loadTexts:unicastRoutesV4Gateway.setStatus(_A)
_UnicastRoutesMTU_Type=Counter32
_UnicastRoutesMTU_Object=MibTableColumn
unicastRoutesMTU=_UnicastRoutesMTU_Object((1,3,6,1,4,1,1429,2,2,5,40,3,1,6),_UnicastRoutesMTU_Type())
unicastRoutesMTU.setMaxAccess(_C)
if mibBuilder.loadTexts:unicastRoutesMTU.setStatus(_A)
_UnicastRoutesTTL_Type=Counter32
_UnicastRoutesTTL_Object=MibTableColumn
unicastRoutesTTL=_UnicastRoutesTTL_Object((1,3,6,1,4,1,1429,2,2,5,40,3,1,7),_UnicastRoutesTTL_Type())
unicastRoutesTTL.setMaxAccess(_C)
if mibBuilder.loadTexts:unicastRoutesTTL.setStatus(_A)
class _UnicastRoutesGWOrHost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('gateway',1),('host',2)))
_UnicastRoutesGWOrHost_Type.__name__=_B
_UnicastRoutesGWOrHost_Object=MibTableColumn
unicastRoutesGWOrHost=_UnicastRoutesGWOrHost_Object((1,3,6,1,4,1,1429,2,2,5,40,3,1,8),_UnicastRoutesGWOrHost_Type())
unicastRoutesGWOrHost.setMaxAccess(_C)
if mibBuilder.loadTexts:unicastRoutesGWOrHost.setStatus(_A)
class _UnicastRoutesType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dynamic',1),('static',2)))
_UnicastRoutesType_Type.__name__=_B
_UnicastRoutesType_Object=MibTableColumn
unicastRoutesType=_UnicastRoutesType_Object((1,3,6,1,4,1,1429,2,2,5,40,3,1,9),_UnicastRoutesType_Type())
unicastRoutesType.setMaxAccess(_C)
if mibBuilder.loadTexts:unicastRoutesType.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'ciscoDSGRouting':ciscoDSGRouting,'multicastRouteTable':multicastRouteTable,'multicastRouteEntry':multicastRouteEntry,_G:multicastRouteIndex,'multicastRouteV4IPAddr':multicastRouteV4IPAddr,'multicastRouteRowStatus':multicastRouteRowStatus,'staticRouteTable':staticRouteTable,'staticRouteEntry':staticRouteEntry,_H:staticRouteIndex,'staticRouteV4IPAddr':staticRouteV4IPAddr,'staticRouteV4Mask':staticRouteV4Mask,'staticRouteV4Gateway':staticRouteV4Gateway,'staticRoutePort1Enable':staticRoutePort1Enable,'staticRoutePort2Enable':staticRoutePort2Enable,'staticRoutePort3Enable':staticRoutePort3Enable,'staticRouteRowStatus':staticRouteRowStatus,'unicastRoutesTable':unicastRoutesTable,'unicastRoutesEntry':unicastRoutesEntry,_I:unicastRoutesIndex,'unicastRoutesPortID':unicastRoutesPortID,'unicastRoutesV4IPAddr':unicastRoutesV4IPAddr,'unicastRoutesV4Mask':unicastRoutesV4Mask,'unicastRoutesV4Gateway':unicastRoutesV4Gateway,'unicastRoutesMTU':unicastRoutesMTU,'unicastRoutesTTL':unicastRoutesTTL,'unicastRoutesGWOrHost':unicastRoutesGWOrHost,'unicastRoutesType':unicastRoutesType})