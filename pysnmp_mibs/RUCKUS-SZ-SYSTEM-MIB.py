_B='current'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,ifIndex=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','ifIndex')
ruckusSZSystemModule,=mibBuilder.importSymbols('RUCKUS-ROOT-MIB','ruckusSZSystemModule')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
ruckusSZSystemMIB=ModuleIdentity((1,3,6,1,4,1,25053,1,4,1,1))
_RuckusSZSystemObjects_ObjectIdentity=ObjectIdentity
ruckusSZSystemObjects=_RuckusSZSystemObjects_ObjectIdentity((1,3,6,1,4,1,25053,1,4,1,1,1))
_RuckusSZSystemInfo_ObjectIdentity=ObjectIdentity
ruckusSZSystemInfo=_RuckusSZSystemInfo_ObjectIdentity((1,3,6,1,4,1,25053,1,4,1,1,1,1))
_RuckusSZSystemStats_ObjectIdentity=ObjectIdentity
ruckusSZSystemStats=_RuckusSZSystemStats_ObjectIdentity((1,3,6,1,4,1,25053,1,4,1,1,1,15))
_RuckusSZSystemStatsNumAP_Type=Unsigned32
_RuckusSZSystemStatsNumAP_Object=MibScalar
ruckusSZSystemStatsNumAP=_RuckusSZSystemStatsNumAP_Object((1,3,6,1,4,1,25053,1,4,1,1,1,15,1),_RuckusSZSystemStatsNumAP_Type())
ruckusSZSystemStatsNumAP.setMaxAccess(_A)
if mibBuilder.loadTexts:ruckusSZSystemStatsNumAP.setStatus(_B)
_RuckusSZSystemStatsNumSta_Type=Unsigned32
_RuckusSZSystemStatsNumSta_Object=MibScalar
ruckusSZSystemStatsNumSta=_RuckusSZSystemStatsNumSta_Object((1,3,6,1,4,1,25053,1,4,1,1,1,15,2),_RuckusSZSystemStatsNumSta_Type())
ruckusSZSystemStatsNumSta.setMaxAccess(_A)
if mibBuilder.loadTexts:ruckusSZSystemStatsNumSta.setStatus(_B)
_RuckusSZSystemStatsWLANTotalRxPkts_Type=Counter64
_RuckusSZSystemStatsWLANTotalRxPkts_Object=MibScalar
ruckusSZSystemStatsWLANTotalRxPkts=_RuckusSZSystemStatsWLANTotalRxPkts_Object((1,3,6,1,4,1,25053,1,4,1,1,1,15,5),_RuckusSZSystemStatsWLANTotalRxPkts_Type())
ruckusSZSystemStatsWLANTotalRxPkts.setMaxAccess(_A)
if mibBuilder.loadTexts:ruckusSZSystemStatsWLANTotalRxPkts.setStatus(_B)
_RuckusSZSystemStatsWLANTotalRxBytes_Type=Counter64
_RuckusSZSystemStatsWLANTotalRxBytes_Object=MibScalar
ruckusSZSystemStatsWLANTotalRxBytes=_RuckusSZSystemStatsWLANTotalRxBytes_Object((1,3,6,1,4,1,25053,1,4,1,1,1,15,6),_RuckusSZSystemStatsWLANTotalRxBytes_Type())
ruckusSZSystemStatsWLANTotalRxBytes.setMaxAccess(_A)
if mibBuilder.loadTexts:ruckusSZSystemStatsWLANTotalRxBytes.setStatus(_B)
_RuckusSZSystemStatsWLANTotalRxMulticast_Type=Counter64
_RuckusSZSystemStatsWLANTotalRxMulticast_Object=MibScalar
ruckusSZSystemStatsWLANTotalRxMulticast=_RuckusSZSystemStatsWLANTotalRxMulticast_Object((1,3,6,1,4,1,25053,1,4,1,1,1,15,7),_RuckusSZSystemStatsWLANTotalRxMulticast_Type())
ruckusSZSystemStatsWLANTotalRxMulticast.setMaxAccess(_A)
if mibBuilder.loadTexts:ruckusSZSystemStatsWLANTotalRxMulticast.setStatus(_B)
_RuckusSZSystemStatsWLANTotalTxPkts_Type=Counter64
_RuckusSZSystemStatsWLANTotalTxPkts_Object=MibScalar
ruckusSZSystemStatsWLANTotalTxPkts=_RuckusSZSystemStatsWLANTotalTxPkts_Object((1,3,6,1,4,1,25053,1,4,1,1,1,15,8),_RuckusSZSystemStatsWLANTotalTxPkts_Type())
ruckusSZSystemStatsWLANTotalTxPkts.setMaxAccess(_A)
if mibBuilder.loadTexts:ruckusSZSystemStatsWLANTotalTxPkts.setStatus(_B)
_RuckusSZSystemStatsWLANTotalTxBytes_Type=Counter64
_RuckusSZSystemStatsWLANTotalTxBytes_Object=MibScalar
ruckusSZSystemStatsWLANTotalTxBytes=_RuckusSZSystemStatsWLANTotalTxBytes_Object((1,3,6,1,4,1,25053,1,4,1,1,1,15,9),_RuckusSZSystemStatsWLANTotalTxBytes_Type())
ruckusSZSystemStatsWLANTotalTxBytes.setMaxAccess(_A)
if mibBuilder.loadTexts:ruckusSZSystemStatsWLANTotalTxBytes.setStatus(_B)
_RuckusSZSystemStatsWLANTotalTxMulticast_Type=Counter64
_RuckusSZSystemStatsWLANTotalTxMulticast_Object=MibScalar
ruckusSZSystemStatsWLANTotalTxMulticast=_RuckusSZSystemStatsWLANTotalTxMulticast_Object((1,3,6,1,4,1,25053,1,4,1,1,1,15,10),_RuckusSZSystemStatsWLANTotalTxMulticast_Type())
ruckusSZSystemStatsWLANTotalTxMulticast.setMaxAccess(_A)
if mibBuilder.loadTexts:ruckusSZSystemStatsWLANTotalTxMulticast.setStatus(_B)
_RuckusSZSystemStatsWLANTotalTxFail_Type=Counter64
_RuckusSZSystemStatsWLANTotalTxFail_Object=MibScalar
ruckusSZSystemStatsWLANTotalTxFail=_RuckusSZSystemStatsWLANTotalTxFail_Object((1,3,6,1,4,1,25053,1,4,1,1,1,15,11),_RuckusSZSystemStatsWLANTotalTxFail_Type())
ruckusSZSystemStatsWLANTotalTxFail.setMaxAccess(_A)
if mibBuilder.loadTexts:ruckusSZSystemStatsWLANTotalTxFail.setStatus(_B)
_RuckusSZSystemStatsWLANTotalTxRetry_Type=Counter64
_RuckusSZSystemStatsWLANTotalTxRetry_Object=MibScalar
ruckusSZSystemStatsWLANTotalTxRetry=_RuckusSZSystemStatsWLANTotalTxRetry_Object((1,3,6,1,4,1,25053,1,4,1,1,1,15,12),_RuckusSZSystemStatsWLANTotalTxRetry_Type())
ruckusSZSystemStatsWLANTotalTxRetry.setMaxAccess(_A)
if mibBuilder.loadTexts:ruckusSZSystemStatsWLANTotalTxRetry.setStatus(_B)
_RuckusSZSystemStatsSerialNumber_Type=DisplayString
_RuckusSZSystemStatsSerialNumber_Object=MibScalar
ruckusSZSystemStatsSerialNumber=_RuckusSZSystemStatsSerialNumber_Object((1,3,6,1,4,1,25053,1,4,1,1,1,15,13),_RuckusSZSystemStatsSerialNumber_Type())
ruckusSZSystemStatsSerialNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:ruckusSZSystemStatsSerialNumber.setStatus(_B)
mibBuilder.exportSymbols('RUCKUS-SZ-SYSTEM-MIB',**{'ruckusSZSystemMIB':ruckusSZSystemMIB,'ruckusSZSystemObjects':ruckusSZSystemObjects,'ruckusSZSystemInfo':ruckusSZSystemInfo,'ruckusSZSystemStats':ruckusSZSystemStats,'ruckusSZSystemStatsNumAP':ruckusSZSystemStatsNumAP,'ruckusSZSystemStatsNumSta':ruckusSZSystemStatsNumSta,'ruckusSZSystemStatsWLANTotalRxPkts':ruckusSZSystemStatsWLANTotalRxPkts,'ruckusSZSystemStatsWLANTotalRxBytes':ruckusSZSystemStatsWLANTotalRxBytes,'ruckusSZSystemStatsWLANTotalRxMulticast':ruckusSZSystemStatsWLANTotalRxMulticast,'ruckusSZSystemStatsWLANTotalTxPkts':ruckusSZSystemStatsWLANTotalTxPkts,'ruckusSZSystemStatsWLANTotalTxBytes':ruckusSZSystemStatsWLANTotalTxBytes,'ruckusSZSystemStatsWLANTotalTxMulticast':ruckusSZSystemStatsWLANTotalTxMulticast,'ruckusSZSystemStatsWLANTotalTxFail':ruckusSZSystemStatsWLANTotalTxFail,'ruckusSZSystemStatsWLANTotalTxRetry':ruckusSZSystemStatsWLANTotalTxRetry,'ruckusSZSystemStatsSerialNumber':ruckusSZSystemStatsSerialNumber})