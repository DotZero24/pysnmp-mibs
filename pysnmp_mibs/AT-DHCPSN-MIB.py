_S='atArpsecVioType'
_R='atArpsecVid'
_Q='atArpsecSrcMac'
_P='atArpsecClientIP'
_O='atDhcpsnVioType'
_N='atDhcpsnChaddr'
_M='atDhcpsnSiaddr'
_L='atDhcpsnGiaddr'
_K='atDhcpsnYiaddr'
_J='atDhcpsnCiaddr'
_I='atDhcpsnOpcode'
_H='atDhcpsnSmac'
_G='atDhcpsnVid'
_F='atArpsecIfIndex'
_E='atDhcpsnIfIndex'
_D='Integer32'
_C='read-only'
_B='AT-DHCPSN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
modules,=mibBuilder.importSymbols('AT-SMI-MIB','modules')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
atDhcpsn=ModuleIdentity((1,3,6,1,4,1,207,8,4,4,4,537))
if mibBuilder.loadTexts:atDhcpsn.setRevisions(('2010-09-07 00:00','2010-06-14 04:45','2010-02-09 01:30','2009-12-10 01:30'))
_AtDhcpsnEvents_ObjectIdentity=ObjectIdentity
atDhcpsnEvents=_AtDhcpsnEvents_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,537,0))
_AtDhcpsnVariablesTable_Object=MibTable
atDhcpsnVariablesTable=_AtDhcpsnVariablesTable_Object((1,3,6,1,4,1,207,8,4,4,4,537,1))
if mibBuilder.loadTexts:atDhcpsnVariablesTable.setStatus(_A)
_AtDhcpsnVariablesEntry_Object=MibTableRow
atDhcpsnVariablesEntry=_AtDhcpsnVariablesEntry_Object((1,3,6,1,4,1,207,8,4,4,4,537,1,1))
atDhcpsnVariablesEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:atDhcpsnVariablesEntry.setStatus(_A)
class _AtDhcpsnIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_AtDhcpsnIfIndex_Type.__name__=_D
_AtDhcpsnIfIndex_Object=MibTableColumn
atDhcpsnIfIndex=_AtDhcpsnIfIndex_Object((1,3,6,1,4,1,207,8,4,4,4,537,1,1,1),_AtDhcpsnIfIndex_Type())
atDhcpsnIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:atDhcpsnIfIndex.setStatus(_A)
_AtDhcpsnVid_Type=Integer32
_AtDhcpsnVid_Object=MibTableColumn
atDhcpsnVid=_AtDhcpsnVid_Object((1,3,6,1,4,1,207,8,4,4,4,537,1,1,2),_AtDhcpsnVid_Type())
atDhcpsnVid.setMaxAccess(_C)
if mibBuilder.loadTexts:atDhcpsnVid.setStatus(_A)
_AtDhcpsnSmac_Type=DisplayString
_AtDhcpsnSmac_Object=MibTableColumn
atDhcpsnSmac=_AtDhcpsnSmac_Object((1,3,6,1,4,1,207,8,4,4,4,537,1,1,3),_AtDhcpsnSmac_Type())
atDhcpsnSmac.setMaxAccess(_C)
if mibBuilder.loadTexts:atDhcpsnSmac.setStatus(_A)
class _AtDhcpsnOpcode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('bootpRequest',1),('bootpReply',2)))
_AtDhcpsnOpcode_Type.__name__=_D
_AtDhcpsnOpcode_Object=MibTableColumn
atDhcpsnOpcode=_AtDhcpsnOpcode_Object((1,3,6,1,4,1,207,8,4,4,4,537,1,1,4),_AtDhcpsnOpcode_Type())
atDhcpsnOpcode.setMaxAccess(_C)
if mibBuilder.loadTexts:atDhcpsnOpcode.setStatus(_A)
_AtDhcpsnCiaddr_Type=IpAddress
_AtDhcpsnCiaddr_Object=MibTableColumn
atDhcpsnCiaddr=_AtDhcpsnCiaddr_Object((1,3,6,1,4,1,207,8,4,4,4,537,1,1,5),_AtDhcpsnCiaddr_Type())
atDhcpsnCiaddr.setMaxAccess(_C)
if mibBuilder.loadTexts:atDhcpsnCiaddr.setStatus(_A)
_AtDhcpsnYiaddr_Type=IpAddress
_AtDhcpsnYiaddr_Object=MibTableColumn
atDhcpsnYiaddr=_AtDhcpsnYiaddr_Object((1,3,6,1,4,1,207,8,4,4,4,537,1,1,6),_AtDhcpsnYiaddr_Type())
atDhcpsnYiaddr.setMaxAccess(_C)
if mibBuilder.loadTexts:atDhcpsnYiaddr.setStatus(_A)
_AtDhcpsnGiaddr_Type=IpAddress
_AtDhcpsnGiaddr_Object=MibTableColumn
atDhcpsnGiaddr=_AtDhcpsnGiaddr_Object((1,3,6,1,4,1,207,8,4,4,4,537,1,1,7),_AtDhcpsnGiaddr_Type())
atDhcpsnGiaddr.setMaxAccess(_C)
if mibBuilder.loadTexts:atDhcpsnGiaddr.setStatus(_A)
_AtDhcpsnSiaddr_Type=IpAddress
_AtDhcpsnSiaddr_Object=MibTableColumn
atDhcpsnSiaddr=_AtDhcpsnSiaddr_Object((1,3,6,1,4,1,207,8,4,4,4,537,1,1,8),_AtDhcpsnSiaddr_Type())
atDhcpsnSiaddr.setMaxAccess(_C)
if mibBuilder.loadTexts:atDhcpsnSiaddr.setStatus(_A)
_AtDhcpsnChaddr_Type=DisplayString
_AtDhcpsnChaddr_Object=MibTableColumn
atDhcpsnChaddr=_AtDhcpsnChaddr_Object((1,3,6,1,4,1,207,8,4,4,4,537,1,1,9),_AtDhcpsnChaddr_Type())
atDhcpsnChaddr.setMaxAccess(_C)
if mibBuilder.loadTexts:atDhcpsnChaddr.setStatus(_A)
class _AtDhcpsnVioType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*(('invalidBootp',1),('invalidDhcpAck',2),('invalidDhcpRelDec',3),('invalidIp',4),('maxBindExceeded',5),('opt82InsertErr',6),('opt82RxInvalid',7),('opt82RxUntrusted',8),('opt82TxUntrusted',9),('replyRxUntrusted',10),('srcMacChaddrMismatch',11),('staticEntryExisted',12),('dbAddErr',13)))
_AtDhcpsnVioType_Type.__name__=_D
_AtDhcpsnVioType_Object=MibTableColumn
atDhcpsnVioType=_AtDhcpsnVioType_Object((1,3,6,1,4,1,207,8,4,4,4,537,1,1,10),_AtDhcpsnVioType_Type())
atDhcpsnVioType.setMaxAccess(_C)
if mibBuilder.loadTexts:atDhcpsnVioType.setStatus(_A)
_AtArpsecVariablesTable_Object=MibTable
atArpsecVariablesTable=_AtArpsecVariablesTable_Object((1,3,6,1,4,1,207,8,4,4,4,537,2))
if mibBuilder.loadTexts:atArpsecVariablesTable.setStatus(_A)
_AtArpsecVariablesEntry_Object=MibTableRow
atArpsecVariablesEntry=_AtArpsecVariablesEntry_Object((1,3,6,1,4,1,207,8,4,4,4,537,2,1))
atArpsecVariablesEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:atArpsecVariablesEntry.setStatus(_A)
class _AtArpsecIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_AtArpsecIfIndex_Type.__name__=_D
_AtArpsecIfIndex_Object=MibTableColumn
atArpsecIfIndex=_AtArpsecIfIndex_Object((1,3,6,1,4,1,207,8,4,4,4,537,2,1,1),_AtArpsecIfIndex_Type())
atArpsecIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:atArpsecIfIndex.setStatus(_A)
_AtArpsecClientIP_Type=IpAddress
_AtArpsecClientIP_Object=MibTableColumn
atArpsecClientIP=_AtArpsecClientIP_Object((1,3,6,1,4,1,207,8,4,4,4,537,2,1,2),_AtArpsecClientIP_Type())
atArpsecClientIP.setMaxAccess(_C)
if mibBuilder.loadTexts:atArpsecClientIP.setStatus(_A)
_AtArpsecSrcMac_Type=DisplayString
_AtArpsecSrcMac_Object=MibTableColumn
atArpsecSrcMac=_AtArpsecSrcMac_Object((1,3,6,1,4,1,207,8,4,4,4,537,2,1,3),_AtArpsecSrcMac_Type())
atArpsecSrcMac.setMaxAccess(_C)
if mibBuilder.loadTexts:atArpsecSrcMac.setStatus(_A)
_AtArpsecVid_Type=Integer32
_AtArpsecVid_Object=MibTableColumn
atArpsecVid=_AtArpsecVid_Object((1,3,6,1,4,1,207,8,4,4,4,537,2,1,4),_AtArpsecVid_Type())
atArpsecVid.setMaxAccess(_C)
if mibBuilder.loadTexts:atArpsecVid.setStatus(_A)
class _AtArpsecVioType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('srcIpNotFound',1),('badVLAN',2),('badPort',3),('srcIpNotAllocated',4)))
_AtArpsecVioType_Type.__name__=_D
_AtArpsecVioType_Object=MibTableColumn
atArpsecVioType=_AtArpsecVioType_Object((1,3,6,1,4,1,207,8,4,4,4,537,2,1,5),_AtArpsecVioType_Type())
atArpsecVioType.setMaxAccess(_C)
if mibBuilder.loadTexts:atArpsecVioType.setStatus(_A)
atDhcpsnTrap=NotificationType((1,3,6,1,4,1,207,8,4,4,4,537,0,1))
atDhcpsnTrap.setObjects(*((_B,_E),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:atDhcpsnTrap.setStatus(_A)
atArpsecTrap=NotificationType((1,3,6,1,4,1,207,8,4,4,4,537,0,2))
atArpsecTrap.setObjects(*((_B,_F),(_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:atArpsecTrap.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'atDhcpsn':atDhcpsn,'atDhcpsnEvents':atDhcpsnEvents,'atDhcpsnTrap':atDhcpsnTrap,'atArpsecTrap':atArpsecTrap,'atDhcpsnVariablesTable':atDhcpsnVariablesTable,'atDhcpsnVariablesEntry':atDhcpsnVariablesEntry,_E:atDhcpsnIfIndex,_G:atDhcpsnVid,_H:atDhcpsnSmac,_I:atDhcpsnOpcode,_J:atDhcpsnCiaddr,_K:atDhcpsnYiaddr,_L:atDhcpsnGiaddr,_M:atDhcpsnSiaddr,_N:atDhcpsnChaddr,_O:atDhcpsnVioType,'atArpsecVariablesTable':atArpsecVariablesTable,'atArpsecVariablesEntry':atArpsecVariablesEntry,_F:atArpsecIfIndex,_P:atArpsecClientIP,_Q:atArpsecSrcMac,_R:atArpsecVid,_S:atArpsecVioType})