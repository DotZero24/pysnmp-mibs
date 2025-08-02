_E='wwpVoipIndex'
_D='WWP-VOIP-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
wwpModules,=mibBuilder.importSymbols('WWP-SMI','wwpModules')
wwpVoipMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,15))
if mibBuilder.loadTexts:wwpVoipMIB.setRevisions(('2001-04-03 17:00',))
_WwpVoipMIBObjects_ObjectIdentity=ObjectIdentity
wwpVoipMIBObjects=_WwpVoipMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,15,1))
_WwpVoip_ObjectIdentity=ObjectIdentity
wwpVoip=_WwpVoip_ObjectIdentity((1,3,6,1,4,1,6141,2,15,1,1))
_WwpVoipTable_Object=MibTable
wwpVoipTable=_WwpVoipTable_Object((1,3,6,1,4,1,6141,2,15,1,1,1))
if mibBuilder.loadTexts:wwpVoipTable.setStatus(_A)
_WwpVoipEntry_Object=MibTableRow
wwpVoipEntry=_WwpVoipEntry_Object((1,3,6,1,4,1,6141,2,15,1,1,1,1))
wwpVoipEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:wwpVoipEntry.setStatus(_A)
class _WwpVoipIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpVoipIndex_Type.__name__=_C
_WwpVoipIndex_Object=MibTableColumn
wwpVoipIndex=_WwpVoipIndex_Object((1,3,6,1,4,1,6141,2,15,1,1,1,1,1),_WwpVoipIndex_Type())
wwpVoipIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpVoipIndex.setStatus(_A)
_WwpVoipDownLoaderVersion_Type=DisplayString
_WwpVoipDownLoaderVersion_Object=MibTableColumn
wwpVoipDownLoaderVersion=_WwpVoipDownLoaderVersion_Object((1,3,6,1,4,1,6141,2,15,1,1,1,1,2),_WwpVoipDownLoaderVersion_Type())
wwpVoipDownLoaderVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpVoipDownLoaderVersion.setStatus(_A)
_WwpVoipApplicationVersion_Type=DisplayString
_WwpVoipApplicationVersion_Object=MibTableColumn
wwpVoipApplicationVersion=_WwpVoipApplicationVersion_Object((1,3,6,1,4,1,6141,2,15,1,1,1,1,3),_WwpVoipApplicationVersion_Type())
wwpVoipApplicationVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpVoipApplicationVersion.setStatus(_A)
class _WwpVoipPortNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpVoipPortNum_Type.__name__=_C
_WwpVoipPortNum_Object=MibTableColumn
wwpVoipPortNum=_WwpVoipPortNum_Object((1,3,6,1,4,1,6141,2,15,1,1,1,1,4),_WwpVoipPortNum_Type())
wwpVoipPortNum.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpVoipPortNum.setStatus(_A)
_WwpVoipIpAddr_Type=IpAddress
_WwpVoipIpAddr_Object=MibTableColumn
wwpVoipIpAddr=_WwpVoipIpAddr_Object((1,3,6,1,4,1,6141,2,15,1,1,1,1,5),_WwpVoipIpAddr_Type())
wwpVoipIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpVoipIpAddr.setStatus(_A)
class _WwpVoipNumResets_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_WwpVoipNumResets_Type.__name__=_C
_WwpVoipNumResets_Object=MibTableColumn
wwpVoipNumResets=_WwpVoipNumResets_Object((1,3,6,1,4,1,6141,2,15,1,1,1,1,6),_WwpVoipNumResets_Type())
wwpVoipNumResets.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpVoipNumResets.setStatus(_A)
_WwpVoipCallAgentAddr_Type=IpAddress
_WwpVoipCallAgentAddr_Object=MibTableColumn
wwpVoipCallAgentAddr=_WwpVoipCallAgentAddr_Object((1,3,6,1,4,1,6141,2,15,1,1,1,1,7),_WwpVoipCallAgentAddr_Type())
wwpVoipCallAgentAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpVoipCallAgentAddr.setStatus(_A)
class _WwpVoipResetOp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('none',0),('reset',1)))
_WwpVoipResetOp_Type.__name__=_C
_WwpVoipResetOp_Object=MibTableColumn
wwpVoipResetOp=_WwpVoipResetOp_Object((1,3,6,1,4,1,6141,2,15,1,1,1,1,8),_WwpVoipResetOp_Type())
wwpVoipResetOp.setMaxAccess('read-write')
if mibBuilder.loadTexts:wwpVoipResetOp.setStatus(_A)
_WwpVoipMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
wwpVoipMIBNotificationPrefix=_WwpVoipMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6141,2,15,2))
_WwpVoipMIBNotifications_ObjectIdentity=ObjectIdentity
wwpVoipMIBNotifications=_WwpVoipMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6141,2,15,2,0))
_WwpVoipMIBConformance_ObjectIdentity=ObjectIdentity
wwpVoipMIBConformance=_WwpVoipMIBConformance_ObjectIdentity((1,3,6,1,4,1,6141,2,15,3))
_WwpVoipMIBCompliances_ObjectIdentity=ObjectIdentity
wwpVoipMIBCompliances=_WwpVoipMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6141,2,15,3,1))
_WwpVoipMIBGroups_ObjectIdentity=ObjectIdentity
wwpVoipMIBGroups=_WwpVoipMIBGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,15,3,2))
wwpVoipDiagFailNotification=NotificationType((1,3,6,1,4,1,6141,2,15,2,0,1))
if mibBuilder.loadTexts:wwpVoipDiagFailNotification.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'wwpVoipMIB':wwpVoipMIB,'wwpVoipMIBObjects':wwpVoipMIBObjects,'wwpVoip':wwpVoip,'wwpVoipTable':wwpVoipTable,'wwpVoipEntry':wwpVoipEntry,_E:wwpVoipIndex,'wwpVoipDownLoaderVersion':wwpVoipDownLoaderVersion,'wwpVoipApplicationVersion':wwpVoipApplicationVersion,'wwpVoipPortNum':wwpVoipPortNum,'wwpVoipIpAddr':wwpVoipIpAddr,'wwpVoipNumResets':wwpVoipNumResets,'wwpVoipCallAgentAddr':wwpVoipCallAgentAddr,'wwpVoipResetOp':wwpVoipResetOp,'wwpVoipMIBNotificationPrefix':wwpVoipMIBNotificationPrefix,'wwpVoipMIBNotifications':wwpVoipMIBNotifications,'wwpVoipDiagFailNotification':wwpVoipDiagFailNotification,'wwpVoipMIBConformance':wwpVoipMIBConformance,'wwpVoipMIBCompliances':wwpVoipMIBCompliances,'wwpVoipMIBGroups':wwpVoipMIBGroups})