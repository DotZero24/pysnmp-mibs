_I='pktcDectSipGroup'
_H='pktcDectSipDNDDisActStat'
_G='pktcDectSipSCFDisNewFwdCalls'
_F='pktcDectSipCFVDisActStat'
_E='pktcDectSipCFVDisNewFwdCalls'
_D='read-write'
_C='SnmpAdminString'
_B='PKTC-DECT-SIP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
pktcApplicationMibs,=mibBuilder.importSymbols('CLAB-DEF-MIB','pktcApplicationMibs')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_C)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
pktcDectSipMib=ModuleIdentity((1,3,6,1,4,1,4491,2,2,8,5))
if mibBuilder.loadTexts:pktcDectSipMib.setRevisions(('2009-02-26 00:00',))
_PktcDectSipNotifications_ObjectIdentity=ObjectIdentity
pktcDectSipNotifications=_PktcDectSipNotifications_ObjectIdentity((1,3,6,1,4,1,4491,2,2,8,5,0))
_PktcDectSipObjects_ObjectIdentity=ObjectIdentity
pktcDectSipObjects=_PktcDectSipObjects_ObjectIdentity((1,3,6,1,4,1,4491,2,2,8,5,1))
_PktcDectSipCFVDis_ObjectIdentity=ObjectIdentity
pktcDectSipCFVDis=_PktcDectSipCFVDis_ObjectIdentity((1,3,6,1,4,1,4491,2,2,8,5,1,1))
class _PktcDectSipCFVDisNewFwdCalls_Type(SnmpAdminString):defaultValue=OctetString('')
_PktcDectSipCFVDisNewFwdCalls_Type.__name__=_C
_PktcDectSipCFVDisNewFwdCalls_Object=MibScalar
pktcDectSipCFVDisNewFwdCalls=_PktcDectSipCFVDisNewFwdCalls_Object((1,3,6,1,4,1,4491,2,2,8,5,1,1,1),_PktcDectSipCFVDisNewFwdCalls_Type())
pktcDectSipCFVDisNewFwdCalls.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcDectSipCFVDisNewFwdCalls.setStatus(_A)
class _PktcDectSipCFVDisActStat_Type(SnmpAdminString):defaultValue=OctetString('')
_PktcDectSipCFVDisActStat_Type.__name__=_C
_PktcDectSipCFVDisActStat_Object=MibScalar
pktcDectSipCFVDisActStat=_PktcDectSipCFVDisActStat_Object((1,3,6,1,4,1,4491,2,2,8,5,1,1,2),_PktcDectSipCFVDisActStat_Type())
pktcDectSipCFVDisActStat.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcDectSipCFVDisActStat.setStatus(_A)
_PktcDectSipSCFDis_ObjectIdentity=ObjectIdentity
pktcDectSipSCFDis=_PktcDectSipSCFDis_ObjectIdentity((1,3,6,1,4,1,4491,2,2,8,5,1,2))
class _PktcDectSipSCFDisNewFwdCalls_Type(SnmpAdminString):defaultValue=OctetString('')
_PktcDectSipSCFDisNewFwdCalls_Type.__name__=_C
_PktcDectSipSCFDisNewFwdCalls_Object=MibScalar
pktcDectSipSCFDisNewFwdCalls=_PktcDectSipSCFDisNewFwdCalls_Object((1,3,6,1,4,1,4491,2,2,8,5,1,2,1),_PktcDectSipSCFDisNewFwdCalls_Type())
pktcDectSipSCFDisNewFwdCalls.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcDectSipSCFDisNewFwdCalls.setStatus(_A)
_PktcDectSipDNDDis_ObjectIdentity=ObjectIdentity
pktcDectSipDNDDis=_PktcDectSipDNDDis_ObjectIdentity((1,3,6,1,4,1,4491,2,2,8,5,1,3))
class _PktcDectSipDNDDisActStat_Type(SnmpAdminString):defaultValue=OctetString('')
_PktcDectSipDNDDisActStat_Type.__name__=_C
_PktcDectSipDNDDisActStat_Object=MibScalar
pktcDectSipDNDDisActStat=_PktcDectSipDNDDisActStat_Object((1,3,6,1,4,1,4491,2,2,8,5,1,3,1),_PktcDectSipDNDDisActStat_Type())
pktcDectSipDNDDisActStat.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcDectSipDNDDisActStat.setStatus(_A)
_PktcDectSipMibConformance_ObjectIdentity=ObjectIdentity
pktcDectSipMibConformance=_PktcDectSipMibConformance_ObjectIdentity((1,3,6,1,4,1,4491,2,2,8,5,2))
_PktcDectSipMibCompliances_ObjectIdentity=ObjectIdentity
pktcDectSipMibCompliances=_PktcDectSipMibCompliances_ObjectIdentity((1,3,6,1,4,1,4491,2,2,8,5,2,1))
_PktcDectSipMibGroups_ObjectIdentity=ObjectIdentity
pktcDectSipMibGroups=_PktcDectSipMibGroups_ObjectIdentity((1,3,6,1,4,1,4491,2,2,8,5,2,2))
pktcDectSipGroup=ObjectGroup((1,3,6,1,4,1,4491,2,2,8,5,2,2,1))
pktcDectSipGroup.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:pktcDectSipGroup.setStatus(_A)
pktcDectSipCompliance=ModuleCompliance((1,3,6,1,4,1,4491,2,2,8,5,2,1,1))
pktcDectSipCompliance.setObjects((_B,_I))
if mibBuilder.loadTexts:pktcDectSipCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'pktcDectSipMib':pktcDectSipMib,'pktcDectSipNotifications':pktcDectSipNotifications,'pktcDectSipObjects':pktcDectSipObjects,'pktcDectSipCFVDis':pktcDectSipCFVDis,_E:pktcDectSipCFVDisNewFwdCalls,_F:pktcDectSipCFVDisActStat,'pktcDectSipSCFDis':pktcDectSipSCFDis,_G:pktcDectSipSCFDisNewFwdCalls,'pktcDectSipDNDDis':pktcDectSipDNDDis,_H:pktcDectSipDNDDisActStat,'pktcDectSipMibConformance':pktcDectSipMibConformance,'pktcDectSipMibCompliances':pktcDectSipMibCompliances,'pktcDectSipCompliance':pktcDectSipCompliance,'pktcDectSipMibGroups':pktcDectSipMibGroups,_I:pktcDectSipGroup})