_L='rlBrgMulticastInetManagerVlanTag'
_K='rlBrgMulticastInetManagerIpType'
_J='read-only'
_I='read-write'
_H='rlBrgMulticastManagerVlanTag'
_G='not-accessible'
_F='ip-src-group'
_E='ip-group'
_D='mac-group'
_C='EDGECORE-rlBrgMcMngr-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rnd,=mibBuilder.importSymbols('EDGECORE-MIB','rnd')
InetAddressType,=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressType')
VlanIndex,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rlBrgMcMngr=ModuleIdentity((1,3,6,1,4,1,259,10,1,14,89,117))
if mibBuilder.loadTexts:rlBrgMcMngr.setRevisions(('2006-02-12 00:00','2004-04-19 00:00'))
_RlBrgMulticastManagerTable_Object=MibTable
rlBrgMulticastManagerTable=_RlBrgMulticastManagerTable_Object((1,3,6,1,4,1,259,10,1,14,89,117,1))
if mibBuilder.loadTexts:rlBrgMulticastManagerTable.setStatus(_A)
_RlBrgMulticastManagerEntry_Object=MibTableRow
rlBrgMulticastManagerEntry=_RlBrgMulticastManagerEntry_Object((1,3,6,1,4,1,259,10,1,14,89,117,1,1))
rlBrgMulticastManagerEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:rlBrgMulticastManagerEntry.setStatus(_A)
_RlBrgMulticastManagerVlanTag_Type=VlanIndex
_RlBrgMulticastManagerVlanTag_Object=MibTableColumn
rlBrgMulticastManagerVlanTag=_RlBrgMulticastManagerVlanTag_Object((1,3,6,1,4,1,259,10,1,14,89,117,1,1,1),_RlBrgMulticastManagerVlanTag_Type())
rlBrgMulticastManagerVlanTag.setMaxAccess(_G)
if mibBuilder.loadTexts:rlBrgMulticastManagerVlanTag.setStatus(_A)
class _RlBrgMulticastManagerAdminVlanMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_F,3)))
_RlBrgMulticastManagerAdminVlanMode_Type.__name__=_B
_RlBrgMulticastManagerAdminVlanMode_Object=MibTableColumn
rlBrgMulticastManagerAdminVlanMode=_RlBrgMulticastManagerAdminVlanMode_Object((1,3,6,1,4,1,259,10,1,14,89,117,1,1,2),_RlBrgMulticastManagerAdminVlanMode_Type())
rlBrgMulticastManagerAdminVlanMode.setMaxAccess(_I)
if mibBuilder.loadTexts:rlBrgMulticastManagerAdminVlanMode.setStatus(_A)
class _RlBrgMulticastManagerOperVlanMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_F,3)))
_RlBrgMulticastManagerOperVlanMode_Type.__name__=_B
_RlBrgMulticastManagerOperVlanMode_Object=MibTableColumn
rlBrgMulticastManagerOperVlanMode=_RlBrgMulticastManagerOperVlanMode_Object((1,3,6,1,4,1,259,10,1,14,89,117,1,1,3),_RlBrgMulticastManagerOperVlanMode_Type())
rlBrgMulticastManagerOperVlanMode.setMaxAccess(_J)
if mibBuilder.loadTexts:rlBrgMulticastManagerOperVlanMode.setStatus(_A)
_RlBrgMulticastInetManagerTable_Object=MibTable
rlBrgMulticastInetManagerTable=_RlBrgMulticastInetManagerTable_Object((1,3,6,1,4,1,259,10,1,14,89,117,2))
if mibBuilder.loadTexts:rlBrgMulticastInetManagerTable.setStatus(_A)
_RlBrgMulticastInetManagerEntry_Object=MibTableRow
rlBrgMulticastInetManagerEntry=_RlBrgMulticastInetManagerEntry_Object((1,3,6,1,4,1,259,10,1,14,89,117,2,1))
rlBrgMulticastInetManagerEntry.setIndexNames((0,_C,_K),(0,_C,_L))
if mibBuilder.loadTexts:rlBrgMulticastInetManagerEntry.setStatus(_A)
class _RlBrgMulticastInetManagerIpType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,16)));namedValues=NamedValues(*(('unknown',0),('ipv4',1),('ipv6',2),('dns',16)))
_RlBrgMulticastInetManagerIpType_Type.__name__=_B
_RlBrgMulticastInetManagerIpType_Object=MibTableColumn
rlBrgMulticastInetManagerIpType=_RlBrgMulticastInetManagerIpType_Object((1,3,6,1,4,1,259,10,1,14,89,117,2,1,1),_RlBrgMulticastInetManagerIpType_Type())
rlBrgMulticastInetManagerIpType.setMaxAccess(_G)
if mibBuilder.loadTexts:rlBrgMulticastInetManagerIpType.setStatus(_A)
_RlBrgMulticastInetManagerVlanTag_Type=VlanIndex
_RlBrgMulticastInetManagerVlanTag_Object=MibTableColumn
rlBrgMulticastInetManagerVlanTag=_RlBrgMulticastInetManagerVlanTag_Object((1,3,6,1,4,1,259,10,1,14,89,117,2,1,2),_RlBrgMulticastInetManagerVlanTag_Type())
rlBrgMulticastInetManagerVlanTag.setMaxAccess(_G)
if mibBuilder.loadTexts:rlBrgMulticastInetManagerVlanTag.setStatus(_A)
class _RlBrgMulticastInetManagerAdminVlanMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_F,3)))
_RlBrgMulticastInetManagerAdminVlanMode_Type.__name__=_B
_RlBrgMulticastInetManagerAdminVlanMode_Object=MibTableColumn
rlBrgMulticastInetManagerAdminVlanMode=_RlBrgMulticastInetManagerAdminVlanMode_Object((1,3,6,1,4,1,259,10,1,14,89,117,2,1,3),_RlBrgMulticastInetManagerAdminVlanMode_Type())
rlBrgMulticastInetManagerAdminVlanMode.setMaxAccess(_I)
if mibBuilder.loadTexts:rlBrgMulticastInetManagerAdminVlanMode.setStatus(_A)
class _RlBrgMulticastInetManagerOperVlanMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_F,3)))
_RlBrgMulticastInetManagerOperVlanMode_Type.__name__=_B
_RlBrgMulticastInetManagerOperVlanMode_Object=MibTableColumn
rlBrgMulticastInetManagerOperVlanMode=_RlBrgMulticastInetManagerOperVlanMode_Object((1,3,6,1,4,1,259,10,1,14,89,117,2,1,4),_RlBrgMulticastInetManagerOperVlanMode_Type())
rlBrgMulticastInetManagerOperVlanMode.setMaxAccess(_J)
if mibBuilder.loadTexts:rlBrgMulticastInetManagerOperVlanMode.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'rlBrgMcMngr':rlBrgMcMngr,'rlBrgMulticastManagerTable':rlBrgMulticastManagerTable,'rlBrgMulticastManagerEntry':rlBrgMulticastManagerEntry,_H:rlBrgMulticastManagerVlanTag,'rlBrgMulticastManagerAdminVlanMode':rlBrgMulticastManagerAdminVlanMode,'rlBrgMulticastManagerOperVlanMode':rlBrgMulticastManagerOperVlanMode,'rlBrgMulticastInetManagerTable':rlBrgMulticastInetManagerTable,'rlBrgMulticastInetManagerEntry':rlBrgMulticastInetManagerEntry,_K:rlBrgMulticastInetManagerIpType,_L:rlBrgMulticastInetManagerVlanTag,'rlBrgMulticastInetManagerAdminVlanMode':rlBrgMulticastInetManagerAdminVlanMode,'rlBrgMulticastInetManagerOperVlanMode':rlBrgMulticastInetManagerOperVlanMode})