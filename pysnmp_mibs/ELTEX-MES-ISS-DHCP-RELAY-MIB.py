_F='eltMesIssMIDhcpRelaySrvAddressEntry'
_E='eltMesIssDhcpRelayVlanId'
_D='Integer32'
_C='ELTEX-MES-ISS-DHCP-RELAY-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMIDhcpRelaySrvAddressEntry,=mibBuilder.importSymbols('ARICENT-DHCP-RLY-MI-MIB','fsMIDhcpRelaySrvAddressEntry')
eltMesIss,=mibBuilder.importSymbols('ELTEX-MES-ISS-MIB','eltMesIss')
InetPortNumber,=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetPortNumber')
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
eltMesIssDhcpRelayMIB=ModuleIdentity((1,3,6,1,4,1,35265,1,139,28))
if mibBuilder.loadTexts:eltMesIssDhcpRelayMIB.setRevisions(('2022-06-02 00:00','2021-10-07 00:00'))
_EltMesIssDhcpRelayObjects_ObjectIdentity=ObjectIdentity
eltMesIssDhcpRelayObjects=_EltMesIssDhcpRelayObjects_ObjectIdentity((1,3,6,1,4,1,35265,1,139,28,1))
_EltMesIssDhcpRelayGlobals_ObjectIdentity=ObjectIdentity
eltMesIssDhcpRelayGlobals=_EltMesIssDhcpRelayGlobals_ObjectIdentity((1,3,6,1,4,1,35265,1,139,28,1,1))
_EltMesIssDhcpRelaySrv_ObjectIdentity=ObjectIdentity
eltMesIssDhcpRelaySrv=_EltMesIssDhcpRelaySrv_ObjectIdentity((1,3,6,1,4,1,35265,1,139,28,1,2))
_EltMesIssMIDhcpRelaySrvAddressTable_Object=MibTable
eltMesIssMIDhcpRelaySrvAddressTable=_EltMesIssMIDhcpRelaySrvAddressTable_Object((1,3,6,1,4,1,35265,1,139,28,1,2,1))
if mibBuilder.loadTexts:eltMesIssMIDhcpRelaySrvAddressTable.setStatus(_A)
_EltMesIssMIDhcpRelaySrvAddressEntry_Object=MibTableRow
eltMesIssMIDhcpRelaySrvAddressEntry=_EltMesIssMIDhcpRelaySrvAddressEntry_Object((1,3,6,1,4,1,35265,1,139,28,1,2,1,1))
if mibBuilder.loadTexts:eltMesIssMIDhcpRelaySrvAddressEntry.setStatus(_A)
_EltMesIssMIDhcpRelaySrvSrcPort_Type=InetPortNumber
_EltMesIssMIDhcpRelaySrvSrcPort_Object=MibTableColumn
eltMesIssMIDhcpRelaySrvSrcPort=_EltMesIssMIDhcpRelaySrvSrcPort_Object((1,3,6,1,4,1,35265,1,139,28,1,2,1,1,1),_EltMesIssMIDhcpRelaySrvSrcPort_Type())
eltMesIssMIDhcpRelaySrvSrcPort.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssMIDhcpRelaySrvSrcPort.setStatus(_A)
_EltMesIssMIDhcpRelaySrvDstPort_Type=InetPortNumber
_EltMesIssMIDhcpRelaySrvDstPort_Object=MibTableColumn
eltMesIssMIDhcpRelaySrvDstPort=_EltMesIssMIDhcpRelaySrvDstPort_Object((1,3,6,1,4,1,35265,1,139,28,1,2,1,1,2),_EltMesIssMIDhcpRelaySrvDstPort_Type())
eltMesIssMIDhcpRelaySrvDstPort.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssMIDhcpRelaySrvDstPort.setStatus(_A)
_EltMesIssDhcpRelayVlan_ObjectIdentity=ObjectIdentity
eltMesIssDhcpRelayVlan=_EltMesIssDhcpRelayVlan_ObjectIdentity((1,3,6,1,4,1,35265,1,139,28,1,3))
_EltMesIssDhcpRelayVlanTable_Object=MibTable
eltMesIssDhcpRelayVlanTable=_EltMesIssDhcpRelayVlanTable_Object((1,3,6,1,4,1,35265,1,139,28,1,3,1))
if mibBuilder.loadTexts:eltMesIssDhcpRelayVlanTable.setStatus(_A)
_EltMesIssDhcpRelayVlanEntry_Object=MibTableRow
eltMesIssDhcpRelayVlanEntry=_EltMesIssDhcpRelayVlanEntry_Object((1,3,6,1,4,1,35265,1,139,28,1,3,1,1))
eltMesIssDhcpRelayVlanEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:eltMesIssDhcpRelayVlanEntry.setStatus(_A)
_EltMesIssDhcpRelayVlanId_Type=VlanId
_EltMesIssDhcpRelayVlanId_Object=MibTableColumn
eltMesIssDhcpRelayVlanId=_EltMesIssDhcpRelayVlanId_Object((1,3,6,1,4,1,35265,1,139,28,1,3,1,1,1),_EltMesIssDhcpRelayVlanId_Type())
eltMesIssDhcpRelayVlanId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:eltMesIssDhcpRelayVlanId.setStatus(_A)
class _EltMesIssDhcpRelayVlanStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_EltMesIssDhcpRelayVlanStatus_Type.__name__=_D
_EltMesIssDhcpRelayVlanStatus_Object=MibTableColumn
eltMesIssDhcpRelayVlanStatus=_EltMesIssDhcpRelayVlanStatus_Object((1,3,6,1,4,1,35265,1,139,28,1,3,1,1,2),_EltMesIssDhcpRelayVlanStatus_Type())
eltMesIssDhcpRelayVlanStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssDhcpRelayVlanStatus.setStatus(_A)
fsMIDhcpRelaySrvAddressEntry.registerAugmentions((_C,_F))
eltMesIssMIDhcpRelaySrvAddressEntry.setIndexNames(*fsMIDhcpRelaySrvAddressEntry.getIndexNames())
mibBuilder.exportSymbols(_C,**{'eltMesIssDhcpRelayMIB':eltMesIssDhcpRelayMIB,'eltMesIssDhcpRelayObjects':eltMesIssDhcpRelayObjects,'eltMesIssDhcpRelayGlobals':eltMesIssDhcpRelayGlobals,'eltMesIssDhcpRelaySrv':eltMesIssDhcpRelaySrv,'eltMesIssMIDhcpRelaySrvAddressTable':eltMesIssMIDhcpRelaySrvAddressTable,_F:eltMesIssMIDhcpRelaySrvAddressEntry,'eltMesIssMIDhcpRelaySrvSrcPort':eltMesIssMIDhcpRelaySrvSrcPort,'eltMesIssMIDhcpRelaySrvDstPort':eltMesIssMIDhcpRelaySrvDstPort,'eltMesIssDhcpRelayVlan':eltMesIssDhcpRelayVlan,'eltMesIssDhcpRelayVlanTable':eltMesIssDhcpRelayVlanTable,'eltMesIssDhcpRelayVlanEntry':eltMesIssDhcpRelayVlanEntry,_E:eltMesIssDhcpRelayVlanId,'eltMesIssDhcpRelayVlanStatus':eltMesIssDhcpRelayVlanStatus})