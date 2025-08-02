_I='mitelAppMonTaskCrashedNotif'
_H='mitelApplicationMonFaultDescr'
_G='mitelApplicationMonFaultDateTime'
_F='mitelApplicationMonFaultStatus'
_E='mitelApplicationMonFaultTblIndex'
_D='Integer32'
_C='read-only'
_B='MITEL-APPLICATION-MON-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
mitelApplicationMon=ModuleIdentity((1,3,6,1,4,1,1027,4,11))
if mibBuilder.loadTexts:mitelApplicationMon.setRevisions(('2003-03-24 01:36','2002-04-02 00:00'))
class DateAndTime(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8),ValueSizeConstraint(11,11))
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
_MitelApplicationMonFaultTable_Object=MibTable
mitelApplicationMonFaultTable=_MitelApplicationMonFaultTable_Object((1,3,6,1,4,1,1027,4,11,1))
if mibBuilder.loadTexts:mitelApplicationMonFaultTable.setStatus(_A)
_MitelApplicationMonFaultEntry_Object=MibTableRow
mitelApplicationMonFaultEntry=_MitelApplicationMonFaultEntry_Object((1,3,6,1,4,1,1027,4,11,1,1))
mitelApplicationMonFaultEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:mitelApplicationMonFaultEntry.setStatus(_A)
_MitelApplicationMonFaultTblIndex_Type=Integer32
_MitelApplicationMonFaultTblIndex_Object=MibTableColumn
mitelApplicationMonFaultTblIndex=_MitelApplicationMonFaultTblIndex_Object((1,3,6,1,4,1,1027,4,11,1,1,1),_MitelApplicationMonFaultTblIndex_Type())
mitelApplicationMonFaultTblIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelApplicationMonFaultTblIndex.setStatus(_A)
class _MitelApplicationMonFaultId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('appMonTaskCrashed',1))
_MitelApplicationMonFaultId_Type.__name__=_D
_MitelApplicationMonFaultId_Object=MibTableColumn
mitelApplicationMonFaultId=_MitelApplicationMonFaultId_Object((1,3,6,1,4,1,1027,4,11,1,1,2),_MitelApplicationMonFaultId_Type())
mitelApplicationMonFaultId.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelApplicationMonFaultId.setStatus(_A)
class _MitelApplicationMonFaultStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('set',1),('clear',2),('message',3)))
_MitelApplicationMonFaultStatus_Type.__name__=_D
_MitelApplicationMonFaultStatus_Object=MibTableColumn
mitelApplicationMonFaultStatus=_MitelApplicationMonFaultStatus_Object((1,3,6,1,4,1,1027,4,11,1,1,3),_MitelApplicationMonFaultStatus_Type())
mitelApplicationMonFaultStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelApplicationMonFaultStatus.setStatus(_A)
_MitelApplicationMonFaultOccur_Type=Counter32
_MitelApplicationMonFaultOccur_Object=MibTableColumn
mitelApplicationMonFaultOccur=_MitelApplicationMonFaultOccur_Object((1,3,6,1,4,1,1027,4,11,1,1,4),_MitelApplicationMonFaultOccur_Type())
mitelApplicationMonFaultOccur.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelApplicationMonFaultOccur.setStatus(_A)
_MitelApplicationMonFaultDateTime_Type=DateAndTime
_MitelApplicationMonFaultDateTime_Object=MibTableColumn
mitelApplicationMonFaultDateTime=_MitelApplicationMonFaultDateTime_Object((1,3,6,1,4,1,1027,4,11,1,1,5),_MitelApplicationMonFaultDateTime_Type())
mitelApplicationMonFaultDateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelApplicationMonFaultDateTime.setStatus(_A)
_MitelApplicationMonFaultDescr_Type=DisplayString
_MitelApplicationMonFaultDescr_Object=MibTableColumn
mitelApplicationMonFaultDescr=_MitelApplicationMonFaultDescr_Object((1,3,6,1,4,1,1027,4,11,1,1,6),_MitelApplicationMonFaultDescr_Type())
mitelApplicationMonFaultDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelApplicationMonFaultDescr.setStatus(_A)
mitelAppMonTaskCrashedNotif=NotificationType((1,3,6,1,4,1,1027,1,2,4,0,411))
mitelAppMonTaskCrashedNotif.setObjects(*((_B,_F),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:mitelAppMonTaskCrashedNotif.setStatus(_A)
mitelIpera1000Notifications=NotificationGroup((1,3,6,1,4,1,1027,1,2,4,0))
mitelIpera1000Notifications.setObjects((_B,_I))
if mibBuilder.loadTexts:mitelIpera1000Notifications.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'DateAndTime':DateAndTime,'mitel':mitel,'mitelIdentification':mitelIdentification,'mitelIdCallServers':mitelIdCallServers,'mitelIdCsIpera1000':mitelIdCsIpera1000,'mitelIpera1000Notifications':mitelIpera1000Notifications,_I:mitelAppMonTaskCrashedNotif,'mitelProprietary':mitelProprietary,'mitelApplicationMon':mitelApplicationMon,'mitelApplicationMonFaultTable':mitelApplicationMonFaultTable,'mitelApplicationMonFaultEntry':mitelApplicationMonFaultEntry,_E:mitelApplicationMonFaultTblIndex,'mitelApplicationMonFaultId':mitelApplicationMonFaultId,_F:mitelApplicationMonFaultStatus,'mitelApplicationMonFaultOccur':mitelApplicationMonFaultOccur,_G:mitelApplicationMonFaultDateTime,_H:mitelApplicationMonFaultDescr})