_J='wwpDnsOperServerId'
_I='read-create'
_H='wwpDnsAdminServerId'
_G='read-write'
_F='TruthValue'
_E='WWP-DNS-CLIENT-MIB'
_D='DisplayString'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','RowStatus','TextualConvention',_F)
wwpModules,=mibBuilder.importSymbols('WWP-SMI','wwpModules')
wwpDnsClientMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,49))
if mibBuilder.loadTexts:wwpDnsClientMIB.setRevisions(('2003-03-19 10:12',))
_WwpDnsClientMIBObjects_ObjectIdentity=ObjectIdentity
wwpDnsClientMIBObjects=_WwpDnsClientMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,49,1))
_WwpDnsClient_ObjectIdentity=ObjectIdentity
wwpDnsClient=_WwpDnsClient_ObjectIdentity((1,3,6,1,4,1,6141,2,49,1,1))
class _WwpDnsResolverEnable_Type(TruthValue):defaultValue=1
_WwpDnsResolverEnable_Type.__name__=_F
_WwpDnsResolverEnable_Object=MibScalar
wwpDnsResolverEnable=_WwpDnsResolverEnable_Object((1,3,6,1,4,1,6141,2,49,1,1,1),_WwpDnsResolverEnable_Type())
wwpDnsResolverEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpDnsResolverEnable.setStatus(_A)
class _WwpDnsDomainAdminName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_WwpDnsDomainAdminName_Type.__name__=_D
_WwpDnsDomainAdminName_Object=MibScalar
wwpDnsDomainAdminName=_WwpDnsDomainAdminName_Object((1,3,6,1,4,1,6141,2,49,1,1,2),_WwpDnsDomainAdminName_Type())
wwpDnsDomainAdminName.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpDnsDomainAdminName.setStatus(_A)
class _WwpDnsDomainOperName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_WwpDnsDomainOperName_Type.__name__=_D
_WwpDnsDomainOperName_Object=MibScalar
wwpDnsDomainOperName=_WwpDnsDomainOperName_Object((1,3,6,1,4,1,6141,2,49,1,1,3),_WwpDnsDomainOperName_Type())
wwpDnsDomainOperName.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpDnsDomainOperName.setStatus(_A)
_WwpDnsNameAdminServerTable_Object=MibTable
wwpDnsNameAdminServerTable=_WwpDnsNameAdminServerTable_Object((1,3,6,1,4,1,6141,2,49,1,1,4))
if mibBuilder.loadTexts:wwpDnsNameAdminServerTable.setStatus(_A)
_WwpDnsNameAdminServerEntry_Object=MibTableRow
wwpDnsNameAdminServerEntry=_WwpDnsNameAdminServerEntry_Object((1,3,6,1,4,1,6141,2,49,1,1,4,1))
wwpDnsNameAdminServerEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:wwpDnsNameAdminServerEntry.setStatus(_A)
class _WwpDnsAdminServerId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_WwpDnsAdminServerId_Type.__name__=_C
_WwpDnsAdminServerId_Object=MibTableColumn
wwpDnsAdminServerId=_WwpDnsAdminServerId_Object((1,3,6,1,4,1,6141,2,49,1,1,4,1,1),_WwpDnsAdminServerId_Type())
wwpDnsAdminServerId.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpDnsAdminServerId.setStatus(_A)
_WwpDnsAdminServerAddr_Type=IpAddress
_WwpDnsAdminServerAddr_Object=MibTableColumn
wwpDnsAdminServerAddr=_WwpDnsAdminServerAddr_Object((1,3,6,1,4,1,6141,2,49,1,1,4,1,2),_WwpDnsAdminServerAddr_Type())
wwpDnsAdminServerAddr.setMaxAccess(_I)
if mibBuilder.loadTexts:wwpDnsAdminServerAddr.setStatus(_A)
_WwpDnsAdminServerStatus_Type=RowStatus
_WwpDnsAdminServerStatus_Object=MibTableColumn
wwpDnsAdminServerStatus=_WwpDnsAdminServerStatus_Object((1,3,6,1,4,1,6141,2,49,1,1,4,1,3),_WwpDnsAdminServerStatus_Type())
wwpDnsAdminServerStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:wwpDnsAdminServerStatus.setStatus(_A)
_WwpDnsNameOperServerTable_Object=MibTable
wwpDnsNameOperServerTable=_WwpDnsNameOperServerTable_Object((1,3,6,1,4,1,6141,2,49,1,1,5))
if mibBuilder.loadTexts:wwpDnsNameOperServerTable.setStatus(_A)
_WwpDnsNameOperServerEntry_Object=MibTableRow
wwpDnsNameOperServerEntry=_WwpDnsNameOperServerEntry_Object((1,3,6,1,4,1,6141,2,49,1,1,5,1))
wwpDnsNameOperServerEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:wwpDnsNameOperServerEntry.setStatus(_A)
class _WwpDnsOperServerId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_WwpDnsOperServerId_Type.__name__=_C
_WwpDnsOperServerId_Object=MibTableColumn
wwpDnsOperServerId=_WwpDnsOperServerId_Object((1,3,6,1,4,1,6141,2,49,1,1,5,1,1),_WwpDnsOperServerId_Type())
wwpDnsOperServerId.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpDnsOperServerId.setStatus(_A)
_WwpDnsOperServerAddr_Type=IpAddress
_WwpDnsOperServerAddr_Object=MibTableColumn
wwpDnsOperServerAddr=_WwpDnsOperServerAddr_Object((1,3,6,1,4,1,6141,2,49,1,1,5,1,2),_WwpDnsOperServerAddr_Type())
wwpDnsOperServerAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpDnsOperServerAddr.setStatus(_A)
_WwpDnsClientMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
wwpDnsClientMIBNotificationPrefix=_WwpDnsClientMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6141,2,49,2))
_WwpDnsClientMIBNotifications_ObjectIdentity=ObjectIdentity
wwpDnsClientMIBNotifications=_WwpDnsClientMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6141,2,49,2,0))
_WwpDnsClientMIBConformance_ObjectIdentity=ObjectIdentity
wwpDnsClientMIBConformance=_WwpDnsClientMIBConformance_ObjectIdentity((1,3,6,1,4,1,6141,2,49,3))
_WwpDnsClientMIBCompliances_ObjectIdentity=ObjectIdentity
wwpDnsClientMIBCompliances=_WwpDnsClientMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6141,2,49,3,1))
_WwpDnsClientMIBGroups_ObjectIdentity=ObjectIdentity
wwpDnsClientMIBGroups=_WwpDnsClientMIBGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,49,3,2))
mibBuilder.exportSymbols(_E,**{'wwpDnsClientMIB':wwpDnsClientMIB,'wwpDnsClientMIBObjects':wwpDnsClientMIBObjects,'wwpDnsClient':wwpDnsClient,'wwpDnsResolverEnable':wwpDnsResolverEnable,'wwpDnsDomainAdminName':wwpDnsDomainAdminName,'wwpDnsDomainOperName':wwpDnsDomainOperName,'wwpDnsNameAdminServerTable':wwpDnsNameAdminServerTable,'wwpDnsNameAdminServerEntry':wwpDnsNameAdminServerEntry,_H:wwpDnsAdminServerId,'wwpDnsAdminServerAddr':wwpDnsAdminServerAddr,'wwpDnsAdminServerStatus':wwpDnsAdminServerStatus,'wwpDnsNameOperServerTable':wwpDnsNameOperServerTable,'wwpDnsNameOperServerEntry':wwpDnsNameOperServerEntry,_J:wwpDnsOperServerId,'wwpDnsOperServerAddr':wwpDnsOperServerAddr,'wwpDnsClientMIBNotificationPrefix':wwpDnsClientMIBNotificationPrefix,'wwpDnsClientMIBNotifications':wwpDnsClientMIBNotifications,'wwpDnsClientMIBConformance':wwpDnsClientMIBConformance,'wwpDnsClientMIBCompliances':wwpDnsClientMIBCompliances,'wwpDnsClientMIBGroups':wwpDnsClientMIBGroups})