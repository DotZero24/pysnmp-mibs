_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
Integer32,=mibBuilder.importSymbols('SNMPv2-SMI-v1',_A)
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class AtmPrivateAddrEsi(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
class AtmSelector(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
class AtmVccTrafficType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('bestEffort',1),('reservedBandwidth',2)))
class Bandwidth(Integer32):0
_Ibm_ObjectIdentity=ObjectIdentity
ibm=_Ibm_ObjectIdentity((1,3,6,1,4,1,2))
_IbmProd_ObjectIdentity=ObjectIdentity
ibmProd=_IbmProd_ObjectIdentity((1,3,6,1,4,1,2,6))
_NwaysMSS_ObjectIdentity=ObjectIdentity
nwaysMSS=_NwaysMSS_ObjectIdentity((1,3,6,1,4,1,2,6,118))
_MssCommon_ObjectIdentity=ObjectIdentity
mssCommon=_MssCommon_ObjectIdentity((1,3,6,1,4,1,2,6,118,1))
_MssCommonHWVPD_ObjectIdentity=ObjectIdentity
mssCommonHWVPD=_MssCommonHWVPD_ObjectIdentity((1,3,6,1,4,1,2,6,118,1,1))
_MssCmnSrvrs_ObjectIdentity=ObjectIdentity
mssCmnSrvrs=_MssCmnSrvrs_ObjectIdentity((1,3,6,1,4,1,2,6,118,1,2))
_MssServerLanE_ObjectIdentity=ObjectIdentity
mssServerLanE=_MssServerLanE_ObjectIdentity((1,3,6,1,4,1,2,6,118,1,2,1))
_MssCmnClnts_ObjectIdentity=ObjectIdentity
mssCmnClnts=_MssCmnClnts_ObjectIdentity((1,3,6,1,4,1,2,6,118,1,3))
mibBuilder.exportSymbols('NWAYSMSS-MIB',**{'AtmPrivateAddrEsi':AtmPrivateAddrEsi,'AtmSelector':AtmSelector,'AtmVccTrafficType':AtmVccTrafficType,'Bandwidth':Bandwidth,'ibm':ibm,'ibmProd':ibmProd,'nwaysMSS':nwaysMSS,'mssCommon':mssCommon,'mssCommonHWVPD':mssCommonHWVPD,'mssCmnSrvrs':mssCmnSrvrs,'mssServerLanE':mssServerLanE,'mssCmnClnts':mssCmnClnts})