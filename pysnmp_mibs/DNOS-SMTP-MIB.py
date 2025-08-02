_G='not-accessible'
_F='agentSmtpServerAddr'
_E='agentSmtpServerAddrType'
_D='Integer32'
_C='DNOS-SMTP-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dnOS,=mibBuilder.importSymbols('DELL-REF-MIB','dnOS')
agentInventoryComponentIndex,=mibBuilder.importSymbols('DNOS-INVENTORY-MIB','agentInventoryComponentIndex')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType','InetPortNumber')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
fastPathSmtp=ModuleIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,169))
if mibBuilder.loadTexts:fastPathSmtp.setRevisions(('2022-02-25 00:00',))
_AgentSmtpConfigGroup_ObjectIdentity=ObjectIdentity
agentSmtpConfigGroup=_AgentSmtpConfigGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,169,1))
_AgentSmtpServerConfigGroup_ObjectIdentity=ObjectIdentity
agentSmtpServerConfigGroup=_AgentSmtpServerConfigGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,169,1,1))
_AgentSmtpServerTable_Object=MibTable
agentSmtpServerTable=_AgentSmtpServerTable_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,169,1,1,1))
if mibBuilder.loadTexts:agentSmtpServerTable.setStatus(_A)
_AgentSmtpServerEntry_Object=MibTableRow
agentSmtpServerEntry=_AgentSmtpServerEntry_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,169,1,1,1,1))
agentSmtpServerEntry.setIndexNames((0,_C,_E),(0,_C,_F))
if mibBuilder.loadTexts:agentSmtpServerEntry.setStatus(_A)
_AgentSmtpServerAddrType_Type=InetAddressType
_AgentSmtpServerAddrType_Object=MibTableColumn
agentSmtpServerAddrType=_AgentSmtpServerAddrType_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,169,1,1,1,1,1),_AgentSmtpServerAddrType_Type())
agentSmtpServerAddrType.setMaxAccess(_G)
if mibBuilder.loadTexts:agentSmtpServerAddrType.setStatus(_A)
_AgentSmtpServerAddr_Type=InetAddress
_AgentSmtpServerAddr_Object=MibTableColumn
agentSmtpServerAddr=_AgentSmtpServerAddr_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,169,1,1,1,1,2),_AgentSmtpServerAddr_Type())
agentSmtpServerAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:agentSmtpServerAddr.setStatus(_A)
_AgentSmtpServerPort_Type=InetPortNumber
_AgentSmtpServerPort_Object=MibTableColumn
agentSmtpServerPort=_AgentSmtpServerPort_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,169,1,1,1,1,3),_AgentSmtpServerPort_Type())
agentSmtpServerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSmtpServerPort.setStatus(_A)
class _AgentSmtpServerSecurity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('none',1),('tlsv1',2)))
_AgentSmtpServerSecurity_Type.__name__=_D
_AgentSmtpServerSecurity_Object=MibTableColumn
agentSmtpServerSecurity=_AgentSmtpServerSecurity_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,169,1,1,1,1,4),_AgentSmtpServerSecurity_Type())
agentSmtpServerSecurity.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSmtpServerSecurity.setStatus(_A)
_AgentSmtpServerloginID_Type=DisplayString
_AgentSmtpServerloginID_Object=MibTableColumn
agentSmtpServerloginID=_AgentSmtpServerloginID_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,169,1,1,1,1,5),_AgentSmtpServerloginID_Type())
agentSmtpServerloginID.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSmtpServerloginID.setStatus(_A)
_AgentSmtpServerPassword_Type=DisplayString
_AgentSmtpServerPassword_Object=MibTableColumn
agentSmtpServerPassword=_AgentSmtpServerPassword_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,169,1,1,1,1,6),_AgentSmtpServerPassword_Type())
agentSmtpServerPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSmtpServerPassword.setStatus(_A)
_AgentSmtpServerEntryStatus_Type=RowStatus
_AgentSmtpServerEntryStatus_Object=MibTableColumn
agentSmtpServerEntryStatus=_AgentSmtpServerEntryStatus_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,169,1,1,1,1,7),_AgentSmtpServerEntryStatus_Type())
agentSmtpServerEntryStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:agentSmtpServerEntryStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'fastPathSmtp':fastPathSmtp,'agentSmtpConfigGroup':agentSmtpConfigGroup,'agentSmtpServerConfigGroup':agentSmtpServerConfigGroup,'agentSmtpServerTable':agentSmtpServerTable,'agentSmtpServerEntry':agentSmtpServerEntry,_E:agentSmtpServerAddrType,_F:agentSmtpServerAddr,'agentSmtpServerPort':agentSmtpServerPort,'agentSmtpServerSecurity':agentSmtpServerSecurity,'agentSmtpServerloginID':agentSmtpServerloginID,'agentSmtpServerPassword':agentSmtpServerPassword,'agentSmtpServerEntryStatus':agentSmtpServerEntryStatus})