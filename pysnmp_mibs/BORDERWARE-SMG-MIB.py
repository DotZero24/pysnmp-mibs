_O='bwMailStatsGroup'
_N='mailClean'
_M='mailVirus'
_L='mailReject'
_K='mailSpam'
_J='mailSent'
_I='mailRcvd'
_H='mailInterval'
_G='totalMessages'
_F='deferredMessages'
_E='queuedMessages'
_D='bwMessagesGroup'
_C='read-only'
_B='BORDERWARE-SMG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
borderware,bwProductId,bwProducts=mibBuilder.importSymbols('BORDERWARE-MIB','borderware','bwProductId','bwProducts')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
bwMailFirewall=ModuleIdentity((1,3,6,1,4,1,8673,1,11))
if mibBuilder.loadTexts:bwMailFirewall.setRevisions(('2004-05-26 00:00',))
_BwMailFirewall4_ObjectIdentity=ObjectIdentity
bwMailFirewall4=_BwMailFirewall4_ObjectIdentity((1,3,6,1,4,1,8673,1,2,11))
_BwMailFirewallConformance_ObjectIdentity=ObjectIdentity
bwMailFirewallConformance=_BwMailFirewallConformance_ObjectIdentity((1,3,6,1,4,1,8673,1,11,3))
_BwMailFirewallCompliances_ObjectIdentity=ObjectIdentity
bwMailFirewallCompliances=_BwMailFirewallCompliances_ObjectIdentity((1,3,6,1,4,1,8673,1,11,3,1))
_BwMailFirewallGroups_ObjectIdentity=ObjectIdentity
bwMailFirewallGroups=_BwMailFirewallGroups_ObjectIdentity((1,3,6,1,4,1,8673,1,11,3,2))
_MailEntry_Object=MibTable
mailEntry=_MailEntry_Object((1,3,6,1,4,1,8673,1,11,10,1))
if mibBuilder.loadTexts:mailEntry.setStatus(_A)
_MailInterval_Type=DisplayString
_MailInterval_Object=MibTableColumn
mailInterval=_MailInterval_Object((1,3,6,1,4,1,8673,1,11,10,1,1),_MailInterval_Type())
mailInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:mailInterval.setStatus(_A)
_MailRcvd_Type=Counter32
_MailRcvd_Object=MibTableColumn
mailRcvd=_MailRcvd_Object((1,3,6,1,4,1,8673,1,11,10,1,2),_MailRcvd_Type())
mailRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:mailRcvd.setStatus(_A)
_MailSent_Type=Counter32
_MailSent_Object=MibTableColumn
mailSent=_MailSent_Object((1,3,6,1,4,1,8673,1,11,10,1,3),_MailSent_Type())
mailSent.setMaxAccess(_C)
if mibBuilder.loadTexts:mailSent.setStatus(_A)
_MailSpam_Type=Counter32
_MailSpam_Object=MibTableColumn
mailSpam=_MailSpam_Object((1,3,6,1,4,1,8673,1,11,10,1,4),_MailSpam_Type())
mailSpam.setMaxAccess(_C)
if mibBuilder.loadTexts:mailSpam.setStatus(_A)
_MailReject_Type=Counter32
_MailReject_Object=MibTableColumn
mailReject=_MailReject_Object((1,3,6,1,4,1,8673,1,11,10,1,5),_MailReject_Type())
mailReject.setMaxAccess(_C)
if mibBuilder.loadTexts:mailReject.setStatus(_A)
_MailVirus_Type=Counter32
_MailVirus_Object=MibTableColumn
mailVirus=_MailVirus_Object((1,3,6,1,4,1,8673,1,11,10,1,6),_MailVirus_Type())
mailVirus.setMaxAccess(_C)
if mibBuilder.loadTexts:mailVirus.setStatus(_A)
_MailClean_Type=Counter32
_MailClean_Object=MibTableColumn
mailClean=_MailClean_Object((1,3,6,1,4,1,8673,1,11,10,1,7),_MailClean_Type())
mailClean.setMaxAccess(_C)
if mibBuilder.loadTexts:mailClean.setStatus(_A)
_MailStatus_ObjectIdentity=ObjectIdentity
mailStatus=_MailStatus_ObjectIdentity((1,3,6,1,4,1,8673,1,11,10,2))
if mibBuilder.loadTexts:mailStatus.setStatus(_A)
_QueuedMessages_Type=Counter32
_QueuedMessages_Object=MibScalar
queuedMessages=_QueuedMessages_Object((1,3,6,1,4,1,8673,1,11,10,2,1),_QueuedMessages_Type())
queuedMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:queuedMessages.setStatus(_A)
_DeferredMessages_Type=Counter32
_DeferredMessages_Object=MibScalar
deferredMessages=_DeferredMessages_Object((1,3,6,1,4,1,8673,1,11,10,2,2),_DeferredMessages_Type())
deferredMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:deferredMessages.setStatus(_A)
_TotalMessages_Type=Counter32
_TotalMessages_Object=MibScalar
totalMessages=_TotalMessages_Object((1,3,6,1,4,1,8673,1,11,10,2,3),_TotalMessages_Type())
totalMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:totalMessages.setStatus(_A)
bwMessagesGroup=ObjectGroup((1,3,6,1,4,1,8673,1,11,3,2,1))
bwMessagesGroup.setObjects(*((_B,_E),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:bwMessagesGroup.setStatus(_A)
bwMailStatsGroup=ObjectGroup((1,3,6,1,4,1,8673,1,11,3,2,2))
bwMailStatsGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:bwMailStatsGroup.setStatus(_A)
mailTable=ObjectGroup((1,3,6,1,4,1,8673,1,11,10))
mailTable.setObjects(*((_B,_O),(_B,_D)))
if mibBuilder.loadTexts:mailTable.setStatus(_A)
bwMailFirewallCompliance=ModuleCompliance((1,3,6,1,4,1,8673,1,11,3,1,1))
bwMailFirewallCompliance.setObjects((_B,_D))
if mibBuilder.loadTexts:bwMailFirewallCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'bwMailFirewall4':bwMailFirewall4,'bwMailFirewall':bwMailFirewall,'bwMailFirewallConformance':bwMailFirewallConformance,'bwMailFirewallCompliances':bwMailFirewallCompliances,'bwMailFirewallCompliance':bwMailFirewallCompliance,'bwMailFirewallGroups':bwMailFirewallGroups,_D:bwMessagesGroup,_O:bwMailStatsGroup,'mailTable':mailTable,'mailEntry':mailEntry,_H:mailInterval,_I:mailRcvd,_J:mailSent,_K:mailSpam,_L:mailReject,_M:mailVirus,_N:mailClean,'mailStatus':mailStatus,_E:queuedMessages,_F:deferredMessages,_G:totalMessages})