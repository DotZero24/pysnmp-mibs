_B='current'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,ifIndex=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','ifIndex')
ruckusSCGSystemModule,=mibBuilder.importSymbols('RUCKUS-ROOT-MIB','ruckusSCGSystemModule')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
ruckusSystemMIB=ModuleIdentity((1,3,6,1,4,1,25053,1,3,1,1))
_RuckusSystemObjects_ObjectIdentity=ObjectIdentity
ruckusSystemObjects=_RuckusSystemObjects_ObjectIdentity((1,3,6,1,4,1,25053,1,3,1,1,1))
_RuckusSystemStats_ObjectIdentity=ObjectIdentity
ruckusSystemStats=_RuckusSystemStats_ObjectIdentity((1,3,6,1,4,1,25053,1,3,1,1,1,15))
_RuckusSystemStatsNumAP_Type=Unsigned32
_RuckusSystemStatsNumAP_Object=MibScalar
ruckusSystemStatsNumAP=_RuckusSystemStatsNumAP_Object((1,3,6,1,4,1,25053,1,3,1,1,1,15,1),_RuckusSystemStatsNumAP_Type())
ruckusSystemStatsNumAP.setMaxAccess(_A)
if mibBuilder.loadTexts:ruckusSystemStatsNumAP.setStatus(_B)
_RuckusSystemStatsNumSta_Type=Unsigned32
_RuckusSystemStatsNumSta_Object=MibScalar
ruckusSystemStatsNumSta=_RuckusSystemStatsNumSta_Object((1,3,6,1,4,1,25053,1,3,1,1,1,15,2),_RuckusSystemStatsNumSta_Type())
ruckusSystemStatsNumSta.setMaxAccess(_A)
if mibBuilder.loadTexts:ruckusSystemStatsNumSta.setStatus(_B)
_RuckusSystemStatsWLANTotalRxPkts_Type=Counter64
_RuckusSystemStatsWLANTotalRxPkts_Object=MibScalar
ruckusSystemStatsWLANTotalRxPkts=_RuckusSystemStatsWLANTotalRxPkts_Object((1,3,6,1,4,1,25053,1,3,1,1,1,15,5),_RuckusSystemStatsWLANTotalRxPkts_Type())
ruckusSystemStatsWLANTotalRxPkts.setMaxAccess(_A)
if mibBuilder.loadTexts:ruckusSystemStatsWLANTotalRxPkts.setStatus(_B)
_RuckusSystemStatsWLANTotalRxBytes_Type=Counter64
_RuckusSystemStatsWLANTotalRxBytes_Object=MibScalar
ruckusSystemStatsWLANTotalRxBytes=_RuckusSystemStatsWLANTotalRxBytes_Object((1,3,6,1,4,1,25053,1,3,1,1,1,15,6),_RuckusSystemStatsWLANTotalRxBytes_Type())
ruckusSystemStatsWLANTotalRxBytes.setMaxAccess(_A)
if mibBuilder.loadTexts:ruckusSystemStatsWLANTotalRxBytes.setStatus(_B)
_RuckusSystemStatsWLANTotalRxMulticast_Type=Counter64
_RuckusSystemStatsWLANTotalRxMulticast_Object=MibScalar
ruckusSystemStatsWLANTotalRxMulticast=_RuckusSystemStatsWLANTotalRxMulticast_Object((1,3,6,1,4,1,25053,1,3,1,1,1,15,7),_RuckusSystemStatsWLANTotalRxMulticast_Type())
ruckusSystemStatsWLANTotalRxMulticast.setMaxAccess(_A)
if mibBuilder.loadTexts:ruckusSystemStatsWLANTotalRxMulticast.setStatus(_B)
_RuckusSystemStatsWLANTotalTxPkts_Type=Counter64
_RuckusSystemStatsWLANTotalTxPkts_Object=MibScalar
ruckusSystemStatsWLANTotalTxPkts=_RuckusSystemStatsWLANTotalTxPkts_Object((1,3,6,1,4,1,25053,1,3,1,1,1,15,8),_RuckusSystemStatsWLANTotalTxPkts_Type())
ruckusSystemStatsWLANTotalTxPkts.setMaxAccess(_A)
if mibBuilder.loadTexts:ruckusSystemStatsWLANTotalTxPkts.setStatus(_B)
_RuckusSystemStatsWLANTotalTxBytes_Type=Counter64
_RuckusSystemStatsWLANTotalTxBytes_Object=MibScalar
ruckusSystemStatsWLANTotalTxBytes=_RuckusSystemStatsWLANTotalTxBytes_Object((1,3,6,1,4,1,25053,1,3,1,1,1,15,9),_RuckusSystemStatsWLANTotalTxBytes_Type())
ruckusSystemStatsWLANTotalTxBytes.setMaxAccess(_A)
if mibBuilder.loadTexts:ruckusSystemStatsWLANTotalTxBytes.setStatus(_B)
_RuckusSystemStatsWLANTotalTxMulticast_Type=Counter64
_RuckusSystemStatsWLANTotalTxMulticast_Object=MibScalar
ruckusSystemStatsWLANTotalTxMulticast=_RuckusSystemStatsWLANTotalTxMulticast_Object((1,3,6,1,4,1,25053,1,3,1,1,1,15,10),_RuckusSystemStatsWLANTotalTxMulticast_Type())
ruckusSystemStatsWLANTotalTxMulticast.setMaxAccess(_A)
if mibBuilder.loadTexts:ruckusSystemStatsWLANTotalTxMulticast.setStatus(_B)
_RuckusSystemStatsWLANTotalTxFail_Type=Counter64
_RuckusSystemStatsWLANTotalTxFail_Object=MibScalar
ruckusSystemStatsWLANTotalTxFail=_RuckusSystemStatsWLANTotalTxFail_Object((1,3,6,1,4,1,25053,1,3,1,1,1,15,11),_RuckusSystemStatsWLANTotalTxFail_Type())
ruckusSystemStatsWLANTotalTxFail.setMaxAccess(_A)
if mibBuilder.loadTexts:ruckusSystemStatsWLANTotalTxFail.setStatus(_B)
_RuckusSystemStatsWLANTotalTxRetry_Type=Counter64
_RuckusSystemStatsWLANTotalTxRetry_Object=MibScalar
ruckusSystemStatsWLANTotalTxRetry=_RuckusSystemStatsWLANTotalTxRetry_Object((1,3,6,1,4,1,25053,1,3,1,1,1,15,12),_RuckusSystemStatsWLANTotalTxRetry_Type())
ruckusSystemStatsWLANTotalTxRetry.setMaxAccess(_A)
if mibBuilder.loadTexts:ruckusSystemStatsWLANTotalTxRetry.setStatus(_B)
_RuckusSystemStatsSerialNumber_Type=DisplayString
_RuckusSystemStatsSerialNumber_Object=MibScalar
ruckusSystemStatsSerialNumber=_RuckusSystemStatsSerialNumber_Object((1,3,6,1,4,1,25053,1,3,1,1,1,15,13),_RuckusSystemStatsSerialNumber_Type())
ruckusSystemStatsSerialNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:ruckusSystemStatsSerialNumber.setStatus(_B)
mibBuilder.exportSymbols('RUCKUS-SCG-SYSTEM-MIB',**{'ruckusSystemMIB':ruckusSystemMIB,'ruckusSystemObjects':ruckusSystemObjects,'ruckusSystemStats':ruckusSystemStats,'ruckusSystemStatsNumAP':ruckusSystemStatsNumAP,'ruckusSystemStatsNumSta':ruckusSystemStatsNumSta,'ruckusSystemStatsWLANTotalRxPkts':ruckusSystemStatsWLANTotalRxPkts,'ruckusSystemStatsWLANTotalRxBytes':ruckusSystemStatsWLANTotalRxBytes,'ruckusSystemStatsWLANTotalRxMulticast':ruckusSystemStatsWLANTotalRxMulticast,'ruckusSystemStatsWLANTotalTxPkts':ruckusSystemStatsWLANTotalTxPkts,'ruckusSystemStatsWLANTotalTxBytes':ruckusSystemStatsWLANTotalTxBytes,'ruckusSystemStatsWLANTotalTxMulticast':ruckusSystemStatsWLANTotalTxMulticast,'ruckusSystemStatsWLANTotalTxFail':ruckusSystemStatsWLANTotalTxFail,'ruckusSystemStatsWLANTotalTxRetry':ruckusSystemStatsWLANTotalTxRetry,'ruckusSystemStatsSerialNumber':ruckusSystemStatsSerialNumber})