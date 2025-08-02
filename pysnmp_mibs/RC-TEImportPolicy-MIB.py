_N='rcIPv4ACLRuleID'
_M='rcIPv4ACLName'
_L='rcRefRouteMapIndex'
_K='rcRefRouteMapname'
_J='rcInterfacename'
_I='rcRouteMapIntanceIndex'
_H='rcRouteMapIndex'
_G='rcRouteMapname'
_F='DisplayString'
_E='not-accessible'
_D='RC-TEImportPolicy-MIB'
_C='Unsigned32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rc,=mibBuilder.importSymbols('RC-SMI','rc')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'MacAddress','PhysAddress','RowStatus','TextualConvention')
rcTEImportPolicy=ModuleIdentity((1,3,6,1,4,1,65000,2))
if mibBuilder.loadTexts:rcTEImportPolicy.setRevisions(('2012-12-11 00:00',))
_RcRouteMapTable_Object=MibTable
rcRouteMapTable=_RcRouteMapTable_Object((1,3,6,1,4,1,65000,2,1))
if mibBuilder.loadTexts:rcRouteMapTable.setStatus(_A)
_RcRouteMapEntry_Object=MibTableRow
rcRouteMapEntry=_RcRouteMapEntry_Object((1,3,6,1,4,1,65000,2,1,1))
rcRouteMapEntry.setIndexNames((0,_D,_G),(0,_D,_H),(0,_D,_I))
if mibBuilder.loadTexts:rcRouteMapEntry.setStatus(_A)
class _RcRouteMapname_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_RcRouteMapname_Type.__name__=_F
_RcRouteMapname_Object=MibTableColumn
rcRouteMapname=_RcRouteMapname_Object((1,3,6,1,4,1,65000,2,1,1,1),_RcRouteMapname_Type())
rcRouteMapname.setMaxAccess(_E)
if mibBuilder.loadTexts:rcRouteMapname.setStatus(_A)
class _RcRouteMapIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_RcRouteMapIndex_Type.__name__=_C
_RcRouteMapIndex_Object=MibTableColumn
rcRouteMapIndex=_RcRouteMapIndex_Object((1,3,6,1,4,1,65000,2,1,1,2),_RcRouteMapIndex_Type())
rcRouteMapIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:rcRouteMapIndex.setStatus(_A)
class _RcRouteMapIntanceIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_RcRouteMapIntanceIndex_Type.__name__=_C
_RcRouteMapIntanceIndex_Object=MibTableColumn
rcRouteMapIntanceIndex=_RcRouteMapIntanceIndex_Object((1,3,6,1,4,1,65000,2,1,1,3),_RcRouteMapIntanceIndex_Type())
rcRouteMapIntanceIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:rcRouteMapIntanceIndex.setStatus(_A)
class _RcRouteMapMatchAcl_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_RcRouteMapMatchAcl_Type.__name__=_F
_RcRouteMapMatchAcl_Object=MibTableColumn
rcRouteMapMatchAcl=_RcRouteMapMatchAcl_Object((1,3,6,1,4,1,65000,2,1,1,4),_RcRouteMapMatchAcl_Type())
rcRouteMapMatchAcl.setMaxAccess(_B)
if mibBuilder.loadTexts:rcRouteMapMatchAcl.setStatus(_A)
class _RcRouteMapSetIntfTunnelID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4000))
_RcRouteMapSetIntfTunnelID_Type.__name__=_C
_RcRouteMapSetIntfTunnelID_Object=MibTableColumn
rcRouteMapSetIntfTunnelID=_RcRouteMapSetIntfTunnelID_Object((1,3,6,1,4,1,65000,2,1,1,5),_RcRouteMapSetIntfTunnelID_Type())
rcRouteMapSetIntfTunnelID.setMaxAccess(_B)
if mibBuilder.loadTexts:rcRouteMapSetIntfTunnelID.setStatus(_A)
_RcRouteMapRowSta_Type=RowStatus
_RcRouteMapRowSta_Object=MibTableColumn
rcRouteMapRowSta=_RcRouteMapRowSta_Object((1,3,6,1,4,1,65000,2,1,1,6),_RcRouteMapRowSta_Type())
rcRouteMapRowSta.setMaxAccess(_B)
if mibBuilder.loadTexts:rcRouteMapRowSta.setStatus(_A)
_RcPolicyRouteTable_Object=MibTable
rcPolicyRouteTable=_RcPolicyRouteTable_Object((1,3,6,1,4,1,65000,2,2))
if mibBuilder.loadTexts:rcPolicyRouteTable.setStatus(_A)
_RcPolicyRouteEntry_Object=MibTableRow
rcPolicyRouteEntry=_RcPolicyRouteEntry_Object((1,3,6,1,4,1,65000,2,2,1))
rcPolicyRouteEntry.setIndexNames((0,_D,_J),(0,_D,_K),(0,_D,_L))
if mibBuilder.loadTexts:rcPolicyRouteEntry.setStatus(_A)
class _RcInterfacename_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_RcInterfacename_Type.__name__=_F
_RcInterfacename_Object=MibTableColumn
rcInterfacename=_RcInterfacename_Object((1,3,6,1,4,1,65000,2,2,1,1),_RcInterfacename_Type())
rcInterfacename.setMaxAccess(_E)
if mibBuilder.loadTexts:rcInterfacename.setStatus(_A)
class _RcRefRouteMapname_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_RcRefRouteMapname_Type.__name__=_F
_RcRefRouteMapname_Object=MibTableColumn
rcRefRouteMapname=_RcRefRouteMapname_Object((1,3,6,1,4,1,65000,2,2,1,2),_RcRefRouteMapname_Type())
rcRefRouteMapname.setMaxAccess(_E)
if mibBuilder.loadTexts:rcRefRouteMapname.setStatus(_A)
class _RcRefRouteMapIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_RcRefRouteMapIndex_Type.__name__=_C
_RcRefRouteMapIndex_Object=MibTableColumn
rcRefRouteMapIndex=_RcRefRouteMapIndex_Object((1,3,6,1,4,1,65000,2,2,1,3),_RcRefRouteMapIndex_Type())
rcRefRouteMapIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:rcRefRouteMapIndex.setStatus(_A)
_RcPolicyRouteRowSta_Type=RowStatus
_RcPolicyRouteRowSta_Object=MibTableColumn
rcPolicyRouteRowSta=_RcPolicyRouteRowSta_Object((1,3,6,1,4,1,65000,2,2,1,4),_RcPolicyRouteRowSta_Type())
rcPolicyRouteRowSta.setMaxAccess(_B)
if mibBuilder.loadTexts:rcPolicyRouteRowSta.setStatus(_A)
_RcACLTable_Object=MibTable
rcACLTable=_RcACLTable_Object((1,3,6,1,4,1,65000,2,3))
if mibBuilder.loadTexts:rcACLTable.setStatus(_A)
_RcACLEntry_Object=MibTableRow
rcACLEntry=_RcACLEntry_Object((1,3,6,1,4,1,65000,2,3,1))
rcACLEntry.setIndexNames((0,_D,_M),(0,_D,_N))
if mibBuilder.loadTexts:rcACLEntry.setStatus(_A)
class _RcIPv4ACLName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_RcIPv4ACLName_Type.__name__=_F
_RcIPv4ACLName_Object=MibTableColumn
rcIPv4ACLName=_RcIPv4ACLName_Object((1,3,6,1,4,1,65000,2,3,1,1),_RcIPv4ACLName_Type())
rcIPv4ACLName.setMaxAccess(_E)
if mibBuilder.loadTexts:rcIPv4ACLName.setStatus(_A)
class _RcIPv4ACLRuleID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RcIPv4ACLRuleID_Type.__name__=_C
_RcIPv4ACLRuleID_Object=MibTableColumn
rcIPv4ACLRuleID=_RcIPv4ACLRuleID_Object((1,3,6,1,4,1,65000,2,3,1,2),_RcIPv4ACLRuleID_Type())
rcIPv4ACLRuleID.setMaxAccess(_E)
if mibBuilder.loadTexts:rcIPv4ACLRuleID.setStatus(_A)
_RcIPv4ACLSrcAddr_Type=IpAddress
_RcIPv4ACLSrcAddr_Object=MibTableColumn
rcIPv4ACLSrcAddr=_RcIPv4ACLSrcAddr_Object((1,3,6,1,4,1,65000,2,3,1,3),_RcIPv4ACLSrcAddr_Type())
rcIPv4ACLSrcAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:rcIPv4ACLSrcAddr.setStatus(_A)
_RcIPv4ACLSrcWildcard_Type=IpAddress
_RcIPv4ACLSrcWildcard_Object=MibTableColumn
rcIPv4ACLSrcWildcard=_RcIPv4ACLSrcWildcard_Object((1,3,6,1,4,1,65000,2,3,1,4),_RcIPv4ACLSrcWildcard_Type())
rcIPv4ACLSrcWildcard.setMaxAccess(_B)
if mibBuilder.loadTexts:rcIPv4ACLSrcWildcard.setStatus(_A)
_RcIPv4ACLDestAddr_Type=IpAddress
_RcIPv4ACLDestAddr_Object=MibTableColumn
rcIPv4ACLDestAddr=_RcIPv4ACLDestAddr_Object((1,3,6,1,4,1,65000,2,3,1,5),_RcIPv4ACLDestAddr_Type())
rcIPv4ACLDestAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:rcIPv4ACLDestAddr.setStatus(_A)
_RcIPv4ACLDestWildcard_Type=IpAddress
_RcIPv4ACLDestWildcard_Object=MibTableColumn
rcIPv4ACLDestWildcard=_RcIPv4ACLDestWildcard_Object((1,3,6,1,4,1,65000,2,3,1,6),_RcIPv4ACLDestWildcard_Type())
rcIPv4ACLDestWildcard.setMaxAccess(_B)
if mibBuilder.loadTexts:rcIPv4ACLDestWildcard.setStatus(_A)
class _RcIPv4ACLProtocol_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RcIPv4ACLProtocol_Type.__name__=_C
_RcIPv4ACLProtocol_Object=MibTableColumn
rcIPv4ACLProtocol=_RcIPv4ACLProtocol_Object((1,3,6,1,4,1,65000,2,3,1,7),_RcIPv4ACLProtocol_Type())
rcIPv4ACLProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:rcIPv4ACLProtocol.setStatus(_A)
class _RcIPv4ACLSrcPortBegin_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RcIPv4ACLSrcPortBegin_Type.__name__=_C
_RcIPv4ACLSrcPortBegin_Object=MibTableColumn
rcIPv4ACLSrcPortBegin=_RcIPv4ACLSrcPortBegin_Object((1,3,6,1,4,1,65000,2,3,1,8),_RcIPv4ACLSrcPortBegin_Type())
rcIPv4ACLSrcPortBegin.setMaxAccess(_B)
if mibBuilder.loadTexts:rcIPv4ACLSrcPortBegin.setStatus(_A)
class _RcIPv4ACLSrcPortEnd_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RcIPv4ACLSrcPortEnd_Type.__name__=_C
_RcIPv4ACLSrcPortEnd_Object=MibTableColumn
rcIPv4ACLSrcPortEnd=_RcIPv4ACLSrcPortEnd_Object((1,3,6,1,4,1,65000,2,3,1,9),_RcIPv4ACLSrcPortEnd_Type())
rcIPv4ACLSrcPortEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:rcIPv4ACLSrcPortEnd.setStatus(_A)
class _RcIPv4ACLDestPortBegin_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RcIPv4ACLDestPortBegin_Type.__name__=_C
_RcIPv4ACLDestPortBegin_Object=MibTableColumn
rcIPv4ACLDestPortBegin=_RcIPv4ACLDestPortBegin_Object((1,3,6,1,4,1,65000,2,3,1,10),_RcIPv4ACLDestPortBegin_Type())
rcIPv4ACLDestPortBegin.setMaxAccess(_B)
if mibBuilder.loadTexts:rcIPv4ACLDestPortBegin.setStatus(_A)
class _RcIPv4ACLDestPortEnd_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RcIPv4ACLDestPortEnd_Type.__name__=_C
_RcIPv4ACLDestPortEnd_Object=MibTableColumn
rcIPv4ACLDestPortEnd=_RcIPv4ACLDestPortEnd_Object((1,3,6,1,4,1,65000,2,3,1,11),_RcIPv4ACLDestPortEnd_Type())
rcIPv4ACLDestPortEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:rcIPv4ACLDestPortEnd.setStatus(_A)
class _RcIPv4ACLDSCP_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63),ValueRangeConstraint(255,255))
_RcIPv4ACLDSCP_Type.__name__=_C
_RcIPv4ACLDSCP_Object=MibTableColumn
rcIPv4ACLDSCP=_RcIPv4ACLDSCP_Object((1,3,6,1,4,1,65000,2,3,1,12),_RcIPv4ACLDSCP_Type())
rcIPv4ACLDSCP.setMaxAccess(_B)
if mibBuilder.loadTexts:rcIPv4ACLDSCP.setStatus(_A)
_RcIPV4ACLRowsta_Type=RowStatus
_RcIPV4ACLRowsta_Object=MibTableColumn
rcIPV4ACLRowsta=_RcIPV4ACLRowsta_Object((1,3,6,1,4,1,65000,2,3,1,13),_RcIPV4ACLRowsta_Type())
rcIPV4ACLRowsta.setMaxAccess(_B)
if mibBuilder.loadTexts:rcIPV4ACLRowsta.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'rcTEImportPolicy':rcTEImportPolicy,'rcRouteMapTable':rcRouteMapTable,'rcRouteMapEntry':rcRouteMapEntry,_G:rcRouteMapname,_H:rcRouteMapIndex,_I:rcRouteMapIntanceIndex,'rcRouteMapMatchAcl':rcRouteMapMatchAcl,'rcRouteMapSetIntfTunnelID':rcRouteMapSetIntfTunnelID,'rcRouteMapRowSta':rcRouteMapRowSta,'rcPolicyRouteTable':rcPolicyRouteTable,'rcPolicyRouteEntry':rcPolicyRouteEntry,_J:rcInterfacename,_K:rcRefRouteMapname,_L:rcRefRouteMapIndex,'rcPolicyRouteRowSta':rcPolicyRouteRowSta,'rcACLTable':rcACLTable,'rcACLEntry':rcACLEntry,_M:rcIPv4ACLName,_N:rcIPv4ACLRuleID,'rcIPv4ACLSrcAddr':rcIPv4ACLSrcAddr,'rcIPv4ACLSrcWildcard':rcIPv4ACLSrcWildcard,'rcIPv4ACLDestAddr':rcIPv4ACLDestAddr,'rcIPv4ACLDestWildcard':rcIPv4ACLDestWildcard,'rcIPv4ACLProtocol':rcIPv4ACLProtocol,'rcIPv4ACLSrcPortBegin':rcIPv4ACLSrcPortBegin,'rcIPv4ACLSrcPortEnd':rcIPv4ACLSrcPortEnd,'rcIPv4ACLDestPortBegin':rcIPv4ACLDestPortBegin,'rcIPv4ACLDestPortEnd':rcIPv4ACLDestPortEnd,'rcIPv4ACLDSCP':rcIPv4ACLDSCP,'rcIPV4ACLRowsta':rcIPV4ACLRowsta})