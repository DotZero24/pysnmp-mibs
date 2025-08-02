_E='pktcEnMtaGroup'
_D='pktcEnMtaDevMltplGrantsPerInterval'
_C='Integer32'
_B='PKTC-EN-MTA-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
pktcEnhancements,=mibBuilder.importSymbols('CLAB-DEF-MIB','pktcEnhancements')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
pktcEnMtaMib=ModuleIdentity((1,3,6,1,4,1,4491,2,2,6,1))
if mibBuilder.loadTexts:pktcEnMtaMib.setRevisions(('2005-01-28 00:00',))
_PktcEnMtaMibObjects_ObjectIdentity=ObjectIdentity
pktcEnMtaMibObjects=_PktcEnMtaMibObjects_ObjectIdentity((1,3,6,1,4,1,4491,2,2,6,1,1))
_PktcEnMtaDevBase_ObjectIdentity=ObjectIdentity
pktcEnMtaDevBase=_PktcEnMtaDevBase_ObjectIdentity((1,3,6,1,4,1,4491,2,2,6,1,1,1))
class _PktcEnMtaDevMltplGrantsPerInterval_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enablemgpifunctionality',1),('disablemgpifunctionality',2)))
_PktcEnMtaDevMltplGrantsPerInterval_Type.__name__=_C
_PktcEnMtaDevMltplGrantsPerInterval_Object=MibScalar
pktcEnMtaDevMltplGrantsPerInterval=_PktcEnMtaDevMltplGrantsPerInterval_Object((1,3,6,1,4,1,4491,2,2,6,1,1,1,1),_PktcEnMtaDevMltplGrantsPerInterval_Type())
pktcEnMtaDevMltplGrantsPerInterval.setMaxAccess('read-only')
if mibBuilder.loadTexts:pktcEnMtaDevMltplGrantsPerInterval.setStatus(_A)
_PktcEnMtaDevServer_ObjectIdentity=ObjectIdentity
pktcEnMtaDevServer=_PktcEnMtaDevServer_ObjectIdentity((1,3,6,1,4,1,4491,2,2,6,1,1,2))
_PktcEnMtaDevSecurity_ObjectIdentity=ObjectIdentity
pktcEnMtaDevSecurity=_PktcEnMtaDevSecurity_ObjectIdentity((1,3,6,1,4,1,4491,2,2,6,1,1,3))
_PktcEnMtaNotificationPrefix_ObjectIdentity=ObjectIdentity
pktcEnMtaNotificationPrefix=_PktcEnMtaNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,4491,2,2,6,1,2))
_PktcEnMtaNotification_ObjectIdentity=ObjectIdentity
pktcEnMtaNotification=_PktcEnMtaNotification_ObjectIdentity((1,3,6,1,4,1,4491,2,2,6,1,2,0))
_PktcEnMtaConformance_ObjectIdentity=ObjectIdentity
pktcEnMtaConformance=_PktcEnMtaConformance_ObjectIdentity((1,3,6,1,4,1,4491,2,2,6,1,3))
_PktcEnMtaCompliances_ObjectIdentity=ObjectIdentity
pktcEnMtaCompliances=_PktcEnMtaCompliances_ObjectIdentity((1,3,6,1,4,1,4491,2,2,6,1,3,1))
_PktcEnMtaGroups_ObjectIdentity=ObjectIdentity
pktcEnMtaGroups=_PktcEnMtaGroups_ObjectIdentity((1,3,6,1,4,1,4491,2,2,6,1,3,2))
pktcEnMtaGroup=ObjectGroup((1,3,6,1,4,1,4491,2,2,6,1,3,2,1))
pktcEnMtaGroup.setObjects((_B,_D))
if mibBuilder.loadTexts:pktcEnMtaGroup.setStatus(_A)
pktcEnMtaBasicCompliance=ModuleCompliance((1,3,6,1,4,1,4491,2,2,6,1,3,1,3))
pktcEnMtaBasicCompliance.setObjects((_B,_E))
if mibBuilder.loadTexts:pktcEnMtaBasicCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'pktcEnMtaMib':pktcEnMtaMib,'pktcEnMtaMibObjects':pktcEnMtaMibObjects,'pktcEnMtaDevBase':pktcEnMtaDevBase,_D:pktcEnMtaDevMltplGrantsPerInterval,'pktcEnMtaDevServer':pktcEnMtaDevServer,'pktcEnMtaDevSecurity':pktcEnMtaDevSecurity,'pktcEnMtaNotificationPrefix':pktcEnMtaNotificationPrefix,'pktcEnMtaNotification':pktcEnMtaNotification,'pktcEnMtaConformance':pktcEnMtaConformance,'pktcEnMtaCompliances':pktcEnMtaCompliances,'pktcEnMtaBasicCompliance':pktcEnMtaBasicCompliance,'pktcEnMtaGroups':pktcEnMtaGroups,_E:pktcEnMtaGroup})