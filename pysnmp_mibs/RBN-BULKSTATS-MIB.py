_X='rbnBulkStatsMIBNotificationGroup2'
_W='rbnBulkStatsMIBNotificationGroup'
_V='rbnBulkStatsTrfrFail2'
_U='rbnBulkStatsTrfrFail'
_T='rbnBulkStatsLastTrfrPolicy'
_S='remoteHostFailed'
_R='badFilename'
_Q='loginFailed'
_P='genError'
_O='success'
_N='vacmContextName'
_M='SNMP-VIEW-BASED-ACM-MIB'
_L='SnmpAdminString'
_K='rbnBulkStatsLastTrfrStatus2'
_J='rbnBulkStatsLastTrfrIpAddr2'
_I='rbnBulkStatsLastTrfrIpAddrType2'
_H='rbnBulkStatsLastTrfrStatus'
_G='rbnBulkStatsLastTrfrIpAddr'
_F='rbnBulkStatsLastTrfrIpAddrType'
_E='Integer32'
_D='read-only'
_C='obsolete'
_B='current'
_A='RBN-BULKSTATS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
rbnMgmt,=mibBuilder.importSymbols('RBN-SMI','rbnMgmt')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_L)
vacmContextName,=mibBuilder.importSymbols(_M,_N)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rbnBulkStatsMIB=ModuleIdentity((1,3,6,1,4,1,2352,2,21))
if mibBuilder.loadTexts:rbnBulkStatsMIB.setRevisions(('2003-02-28 00:00','2002-05-03 00:00'))
_RbnBulkStatsMIBNotifications_ObjectIdentity=ObjectIdentity
rbnBulkStatsMIBNotifications=_RbnBulkStatsMIBNotifications_ObjectIdentity((1,3,6,1,4,1,2352,2,21,0))
_RbnBulkStatsMIBObjects_ObjectIdentity=ObjectIdentity
rbnBulkStatsMIBObjects=_RbnBulkStatsMIBObjects_ObjectIdentity((1,3,6,1,4,1,2352,2,21,1))
_RbnBulkStatsLastTrfr_ObjectIdentity=ObjectIdentity
rbnBulkStatsLastTrfr=_RbnBulkStatsLastTrfr_ObjectIdentity((1,3,6,1,4,1,2352,2,21,1,1))
_RbnBulkStatsLastTrfrIpAddrType_Type=InetAddressType
_RbnBulkStatsLastTrfrIpAddrType_Object=MibScalar
rbnBulkStatsLastTrfrIpAddrType=_RbnBulkStatsLastTrfrIpAddrType_Object((1,3,6,1,4,1,2352,2,21,1,1,1),_RbnBulkStatsLastTrfrIpAddrType_Type())
rbnBulkStatsLastTrfrIpAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:rbnBulkStatsLastTrfrIpAddrType.setStatus(_C)
_RbnBulkStatsLastTrfrIpAddr_Type=InetAddress
_RbnBulkStatsLastTrfrIpAddr_Object=MibScalar
rbnBulkStatsLastTrfrIpAddr=_RbnBulkStatsLastTrfrIpAddr_Object((1,3,6,1,4,1,2352,2,21,1,1,2),_RbnBulkStatsLastTrfrIpAddr_Type())
rbnBulkStatsLastTrfrIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:rbnBulkStatsLastTrfrIpAddr.setStatus(_C)
class _RbnBulkStatsLastTrfrStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('none',1),(_O,2),(_P,3),(_Q,4),(_R,5),(_S,6),('other',7)))
_RbnBulkStatsLastTrfrStatus_Type.__name__=_E
_RbnBulkStatsLastTrfrStatus_Object=MibScalar
rbnBulkStatsLastTrfrStatus=_RbnBulkStatsLastTrfrStatus_Object((1,3,6,1,4,1,2352,2,21,1,1,3),_RbnBulkStatsLastTrfrStatus_Type())
rbnBulkStatsLastTrfrStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rbnBulkStatsLastTrfrStatus.setStatus(_C)
_RbnBulkStatsLastTrfrTable_Object=MibTable
rbnBulkStatsLastTrfrTable=_RbnBulkStatsLastTrfrTable_Object((1,3,6,1,4,1,2352,2,21,1,1,4))
if mibBuilder.loadTexts:rbnBulkStatsLastTrfrTable.setStatus(_B)
_RbnBulkStatsLastTrfrEntry_Object=MibTableRow
rbnBulkStatsLastTrfrEntry=_RbnBulkStatsLastTrfrEntry_Object((1,3,6,1,4,1,2352,2,21,1,1,4,1))
rbnBulkStatsLastTrfrEntry.setIndexNames((0,_M,_N),(0,_A,_T))
if mibBuilder.loadTexts:rbnBulkStatsLastTrfrEntry.setStatus(_B)
class _RbnBulkStatsLastTrfrPolicy_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_RbnBulkStatsLastTrfrPolicy_Type.__name__=_L
_RbnBulkStatsLastTrfrPolicy_Object=MibTableColumn
rbnBulkStatsLastTrfrPolicy=_RbnBulkStatsLastTrfrPolicy_Object((1,3,6,1,4,1,2352,2,21,1,1,4,1,1),_RbnBulkStatsLastTrfrPolicy_Type())
rbnBulkStatsLastTrfrPolicy.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:rbnBulkStatsLastTrfrPolicy.setStatus(_B)
_RbnBulkStatsLastTrfrIpAddrType2_Type=InetAddressType
_RbnBulkStatsLastTrfrIpAddrType2_Object=MibTableColumn
rbnBulkStatsLastTrfrIpAddrType2=_RbnBulkStatsLastTrfrIpAddrType2_Object((1,3,6,1,4,1,2352,2,21,1,1,4,1,2),_RbnBulkStatsLastTrfrIpAddrType2_Type())
rbnBulkStatsLastTrfrIpAddrType2.setMaxAccess(_D)
if mibBuilder.loadTexts:rbnBulkStatsLastTrfrIpAddrType2.setStatus(_B)
_RbnBulkStatsLastTrfrIpAddr2_Type=InetAddress
_RbnBulkStatsLastTrfrIpAddr2_Object=MibTableColumn
rbnBulkStatsLastTrfrIpAddr2=_RbnBulkStatsLastTrfrIpAddr2_Object((1,3,6,1,4,1,2352,2,21,1,1,4,1,3),_RbnBulkStatsLastTrfrIpAddr2_Type())
rbnBulkStatsLastTrfrIpAddr2.setMaxAccess(_D)
if mibBuilder.loadTexts:rbnBulkStatsLastTrfrIpAddr2.setStatus(_B)
class _RbnBulkStatsLastTrfrStatus2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('none',1),(_O,2),(_P,3),(_Q,4),(_R,5),(_S,6),('other',7)))
_RbnBulkStatsLastTrfrStatus2_Type.__name__=_E
_RbnBulkStatsLastTrfrStatus2_Object=MibTableColumn
rbnBulkStatsLastTrfrStatus2=_RbnBulkStatsLastTrfrStatus2_Object((1,3,6,1,4,1,2352,2,21,1,1,4,1,4),_RbnBulkStatsLastTrfrStatus2_Type())
rbnBulkStatsLastTrfrStatus2.setMaxAccess(_D)
if mibBuilder.loadTexts:rbnBulkStatsLastTrfrStatus2.setStatus(_B)
_RbnBulkStatsMIBConformance_ObjectIdentity=ObjectIdentity
rbnBulkStatsMIBConformance=_RbnBulkStatsMIBConformance_ObjectIdentity((1,3,6,1,4,1,2352,2,21,2))
_RbnBulkStatsMIBGroups_ObjectIdentity=ObjectIdentity
rbnBulkStatsMIBGroups=_RbnBulkStatsMIBGroups_ObjectIdentity((1,3,6,1,4,1,2352,2,21,2,1))
_RbnBulkStatsMIBCompliances_ObjectIdentity=ObjectIdentity
rbnBulkStatsMIBCompliances=_RbnBulkStatsMIBCompliances_ObjectIdentity((1,3,6,1,4,1,2352,2,21,2,2))
rbnBulkStatsMIBObjectGroup=ObjectGroup((1,3,6,1,4,1,2352,2,21,2,1,1))
rbnBulkStatsMIBObjectGroup.setObjects(*((_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:rbnBulkStatsMIBObjectGroup.setStatus(_C)
rbnBulkStatsMIBObjectGroup2=ObjectGroup((1,3,6,1,4,1,2352,2,21,2,1,3))
rbnBulkStatsMIBObjectGroup2.setObjects(*((_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:rbnBulkStatsMIBObjectGroup2.setStatus(_B)
rbnBulkStatsTrfrFail=NotificationType((1,3,6,1,4,1,2352,2,21,0,1))
rbnBulkStatsTrfrFail.setObjects(*((_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:rbnBulkStatsTrfrFail.setStatus(_C)
rbnBulkStatsTrfrFail2=NotificationType((1,3,6,1,4,1,2352,2,21,0,2))
rbnBulkStatsTrfrFail2.setObjects(*((_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:rbnBulkStatsTrfrFail2.setStatus(_B)
rbnBulkStatsMIBNotificationGroup=NotificationGroup((1,3,6,1,4,1,2352,2,21,2,1,2))
rbnBulkStatsMIBNotificationGroup.setObjects((_A,_U))
if mibBuilder.loadTexts:rbnBulkStatsMIBNotificationGroup.setStatus(_C)
rbnBulkStatsMIBNotificationGroup2=NotificationGroup((1,3,6,1,4,1,2352,2,21,2,1,4))
rbnBulkStatsMIBNotificationGroup2.setObjects((_A,_V))
if mibBuilder.loadTexts:rbnBulkStatsMIBNotificationGroup2.setStatus(_B)
rbnBulkStatsMIBCompliance=ModuleCompliance((1,3,6,1,4,1,2352,2,21,2,2,1))
rbnBulkStatsMIBCompliance.setObjects((_A,_W))
if mibBuilder.loadTexts:rbnBulkStatsMIBCompliance.setStatus(_C)
rbnBulkStatsMIBCompliance2=ModuleCompliance((1,3,6,1,4,1,2352,2,21,2,2,2))
rbnBulkStatsMIBCompliance2.setObjects((_A,_X))
if mibBuilder.loadTexts:rbnBulkStatsMIBCompliance2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'rbnBulkStatsMIB':rbnBulkStatsMIB,'rbnBulkStatsMIBNotifications':rbnBulkStatsMIBNotifications,_U:rbnBulkStatsTrfrFail,_V:rbnBulkStatsTrfrFail2,'rbnBulkStatsMIBObjects':rbnBulkStatsMIBObjects,'rbnBulkStatsLastTrfr':rbnBulkStatsLastTrfr,_F:rbnBulkStatsLastTrfrIpAddrType,_G:rbnBulkStatsLastTrfrIpAddr,_H:rbnBulkStatsLastTrfrStatus,'rbnBulkStatsLastTrfrTable':rbnBulkStatsLastTrfrTable,'rbnBulkStatsLastTrfrEntry':rbnBulkStatsLastTrfrEntry,_T:rbnBulkStatsLastTrfrPolicy,_I:rbnBulkStatsLastTrfrIpAddrType2,_J:rbnBulkStatsLastTrfrIpAddr2,_K:rbnBulkStatsLastTrfrStatus2,'rbnBulkStatsMIBConformance':rbnBulkStatsMIBConformance,'rbnBulkStatsMIBGroups':rbnBulkStatsMIBGroups,'rbnBulkStatsMIBObjectGroup':rbnBulkStatsMIBObjectGroup,_W:rbnBulkStatsMIBNotificationGroup,'rbnBulkStatsMIBObjectGroup2':rbnBulkStatsMIBObjectGroup2,_X:rbnBulkStatsMIBNotificationGroup2,'rbnBulkStatsMIBCompliances':rbnBulkStatsMIBCompliances,'rbnBulkStatsMIBCompliance':rbnBulkStatsMIBCompliance,'rbnBulkStatsMIBCompliance2':rbnBulkStatsMIBCompliance2})