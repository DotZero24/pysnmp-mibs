_I='mitelVoiceMailDiskFullNotif'
_H='mitelVoiceMailDiskNearlyFullNotif'
_G='mitelVoiceMailFaultTblIndex'
_F='mitelVoiceMailFaultOccur'
_E='mitelVoiceMailFaultStatus'
_D='Integer32'
_C='read-only'
_B='MITEL-VOICE-MAIL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
mitelVoiceMail=ModuleIdentity((1,3,6,1,4,1,1027,4,10))
if mibBuilder.loadTexts:mitelVoiceMail.setRevisions(('2002-03-24 11:49','2002-04-02 00:00'))
_Mitel_ObjectIdentity=ObjectIdentity
mitel=_Mitel_ObjectIdentity((1,3,6,1,4,1,1027))
_MitelIdentification_ObjectIdentity=ObjectIdentity
mitelIdentification=_MitelIdentification_ObjectIdentity((1,3,6,1,4,1,1027,1))
_MitelIdCallServers_ObjectIdentity=ObjectIdentity
mitelIdCallServers=_MitelIdCallServers_ObjectIdentity((1,3,6,1,4,1,1027,1,2))
_MitelIdCsIpera1000_ObjectIdentity=ObjectIdentity
mitelIdCsIpera1000=_MitelIdCsIpera1000_ObjectIdentity((1,3,6,1,4,1,1027,1,2,4))
_MitelProprietary_ObjectIdentity=ObjectIdentity
mitelProprietary=_MitelProprietary_ObjectIdentity((1,3,6,1,4,1,1027,4))
_MitelVoiceMailFaultTable_Object=MibTable
mitelVoiceMailFaultTable=_MitelVoiceMailFaultTable_Object((1,3,6,1,4,1,1027,4,10,1))
if mibBuilder.loadTexts:mitelVoiceMailFaultTable.setStatus(_A)
_MitelVoiceMailFaultEntry_Object=MibTableRow
mitelVoiceMailFaultEntry=_MitelVoiceMailFaultEntry_Object((1,3,6,1,4,1,1027,4,10,1,1))
mitelVoiceMailFaultEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:mitelVoiceMailFaultEntry.setStatus(_A)
_MitelVoiceMailFaultTblIndex_Type=Integer32
_MitelVoiceMailFaultTblIndex_Object=MibTableColumn
mitelVoiceMailFaultTblIndex=_MitelVoiceMailFaultTblIndex_Object((1,3,6,1,4,1,1027,4,10,1,1,1),_MitelVoiceMailFaultTblIndex_Type())
mitelVoiceMailFaultTblIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelVoiceMailFaultTblIndex.setStatus(_A)
class _MitelVoiceMailFaultId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('voiceMailDiskNearlyFull',1),('voiceMailDiskFull',2)))
_MitelVoiceMailFaultId_Type.__name__=_D
_MitelVoiceMailFaultId_Object=MibTableColumn
mitelVoiceMailFaultId=_MitelVoiceMailFaultId_Object((1,3,6,1,4,1,1027,4,10,1,1,2),_MitelVoiceMailFaultId_Type())
mitelVoiceMailFaultId.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelVoiceMailFaultId.setStatus(_A)
class _MitelVoiceMailFaultStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('set',1),('clear',2),('message',3)))
_MitelVoiceMailFaultStatus_Type.__name__=_D
_MitelVoiceMailFaultStatus_Object=MibTableColumn
mitelVoiceMailFaultStatus=_MitelVoiceMailFaultStatus_Object((1,3,6,1,4,1,1027,4,10,1,1,3),_MitelVoiceMailFaultStatus_Type())
mitelVoiceMailFaultStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelVoiceMailFaultStatus.setStatus(_A)
_MitelVoiceMailFaultOccur_Type=Counter32
_MitelVoiceMailFaultOccur_Object=MibTableColumn
mitelVoiceMailFaultOccur=_MitelVoiceMailFaultOccur_Object((1,3,6,1,4,1,1027,4,10,1,1,4),_MitelVoiceMailFaultOccur_Type())
mitelVoiceMailFaultOccur.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelVoiceMailFaultOccur.setStatus(_A)
mitelVoiceMailDiskNearlyFullNotif=NotificationType((1,3,6,1,4,1,1027,1,2,4,0,408))
mitelVoiceMailDiskNearlyFullNotif.setObjects(*((_B,_E),(_B,_F)))
if mibBuilder.loadTexts:mitelVoiceMailDiskNearlyFullNotif.setStatus(_A)
mitelVoiceMailDiskFullNotif=NotificationType((1,3,6,1,4,1,1027,1,2,4,0,409))
mitelVoiceMailDiskFullNotif.setObjects(*((_B,_E),(_B,_F)))
if mibBuilder.loadTexts:mitelVoiceMailDiskFullNotif.setStatus(_A)
mitelIpera1000Notifications=NotificationGroup((1,3,6,1,4,1,1027,1,2,4,0))
mitelIpera1000Notifications.setObjects(*((_B,_H),(_B,_I)))
if mibBuilder.loadTexts:mitelIpera1000Notifications.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'mitel':mitel,'mitelIdentification':mitelIdentification,'mitelIdCallServers':mitelIdCallServers,'mitelIdCsIpera1000':mitelIdCsIpera1000,'mitelIpera1000Notifications':mitelIpera1000Notifications,_H:mitelVoiceMailDiskNearlyFullNotif,_I:mitelVoiceMailDiskFullNotif,'mitelProprietary':mitelProprietary,'mitelVoiceMail':mitelVoiceMail,'mitelVoiceMailFaultTable':mitelVoiceMailFaultTable,'mitelVoiceMailFaultEntry':mitelVoiceMailFaultEntry,_G:mitelVoiceMailFaultTblIndex,'mitelVoiceMailFaultId':mitelVoiceMailFaultId,_E:mitelVoiceMailFaultStatus,_F:mitelVoiceMailFaultOccur})