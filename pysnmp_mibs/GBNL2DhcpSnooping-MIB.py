_G='vlanIndex'
_F='read-only'
_E='portIndex'
_D='GBNL2DhcpSnooping-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
gbnL2,=mibBuilder.importSymbols('GREENTECH-MASTER-MIB','gbnL2')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
gbnL3DhcpSnooping=ModuleIdentity((1,3,6,1,4,1,13464,1,2,4,5))
if mibBuilder.loadTexts:gbnL3DhcpSnooping.setRevisions(('1901-05-03 00:00',))
_DhcpsnoopingOnOff_Type=TruthValue
_DhcpsnoopingOnOff_Object=MibScalar
dhcpsnoopingOnOff=_DhcpsnoopingOnOff_Object((1,3,6,1,4,1,13464,1,2,4,5,1),_DhcpsnoopingOnOff_Type())
dhcpsnoopingOnOff.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpsnoopingOnOff.setStatus(_A)
_DhcpsnoopingPortTable_Object=MibTable
dhcpsnoopingPortTable=_DhcpsnoopingPortTable_Object((1,3,6,1,4,1,13464,1,2,4,5,2))
if mibBuilder.loadTexts:dhcpsnoopingPortTable.setStatus(_A)
_DhcpsnoopingPortEntry_Object=MibTableRow
dhcpsnoopingPortEntry=_DhcpsnoopingPortEntry_Object((1,3,6,1,4,1,13464,1,2,4,5,2,1))
dhcpsnoopingPortEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:dhcpsnoopingPortEntry.setStatus(_A)
_PortIndex_Type=Integer32
_PortIndex_Object=MibTableColumn
portIndex=_PortIndex_Object((1,3,6,1,4,1,13464,1,2,4,5,2,1,1),_PortIndex_Type())
portIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:portIndex.setStatus(_A)
class _PortTrustMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('trust',1),('untrust',2)))
_PortTrustMode_Type.__name__=_C
_PortTrustMode_Object=MibTableColumn
portTrustMode=_PortTrustMode_Object((1,3,6,1,4,1,13464,1,2,4,5,2,1,2),_PortTrustMode_Type())
portTrustMode.setMaxAccess(_B)
if mibBuilder.loadTexts:portTrustMode.setStatus(_A)
_PortMaxNum_Type=Integer32
_PortMaxNum_Object=MibTableColumn
portMaxNum=_PortMaxNum_Object((1,3,6,1,4,1,13464,1,2,4,5,2,1,3),_PortMaxNum_Type())
portMaxNum.setMaxAccess(_B)
if mibBuilder.loadTexts:portMaxNum.setStatus(_A)
class _PortIpSourceGuardMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_PortIpSourceGuardMode_Type.__name__=_C
_PortIpSourceGuardMode_Object=MibTableColumn
portIpSourceGuardMode=_PortIpSourceGuardMode_Object((1,3,6,1,4,1,13464,1,2,4,5,2,1,4),_PortIpSourceGuardMode_Type())
portIpSourceGuardMode.setMaxAccess(_B)
if mibBuilder.loadTexts:portIpSourceGuardMode.setStatus(_A)
_DhcpsnoopingVlanTable_Object=MibTable
dhcpsnoopingVlanTable=_DhcpsnoopingVlanTable_Object((1,3,6,1,4,1,13464,1,2,4,5,3))
if mibBuilder.loadTexts:dhcpsnoopingVlanTable.setStatus(_A)
_DhcpsnoopingVlanEntry_Object=MibTableRow
dhcpsnoopingVlanEntry=_DhcpsnoopingVlanEntry_Object((1,3,6,1,4,1,13464,1,2,4,5,3,1))
dhcpsnoopingVlanEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:dhcpsnoopingVlanEntry.setStatus(_A)
class _VlanIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_VlanIndex_Type.__name__=_C
_VlanIndex_Object=MibTableColumn
vlanIndex=_VlanIndex_Object((1,3,6,1,4,1,13464,1,2,4,5,3,1,1),_VlanIndex_Type())
vlanIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:vlanIndex.setStatus(_A)
_VlanMaxNum_Type=Integer32
_VlanMaxNum_Object=MibTableColumn
vlanMaxNum=_VlanMaxNum_Object((1,3,6,1,4,1,13464,1,2,4,5,3,1,2),_VlanMaxNum_Type())
vlanMaxNum.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanMaxNum.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'gbnL3DhcpSnooping':gbnL3DhcpSnooping,'dhcpsnoopingOnOff':dhcpsnoopingOnOff,'dhcpsnoopingPortTable':dhcpsnoopingPortTable,'dhcpsnoopingPortEntry':dhcpsnoopingPortEntry,_E:portIndex,'portTrustMode':portTrustMode,'portMaxNum':portMaxNum,'portIpSourceGuardMode':portIpSourceGuardMode,'dhcpsnoopingVlanTable':dhcpsnoopingVlanTable,'dhcpsnoopingVlanEntry':dhcpsnoopingVlanEntry,_G:vlanIndex,'vlanMaxNum':vlanMaxNum})