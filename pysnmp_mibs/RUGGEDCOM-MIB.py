_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ruggedcom=ModuleIdentity((1,3,6,1,4,1,15004))
if mibBuilder.loadTexts:ruggedcom.setRevisions(('2017-09-20 11:00','2015-04-02 09:00','2012-06-01 17:00','2010-05-27 10:30','2010-03-12 10:30','2008-12-17 13:00','2006-09-09 09:00','2003-02-18 14:00'))
_RuggedcomExperiment_ObjectIdentity=ObjectIdentity
ruggedcomExperiment=_RuggedcomExperiment_ObjectIdentity((1,3,6,1,4,1,15004,1))
if mibBuilder.loadTexts:ruggedcomExperiment.setStatus(_A)
_RuggedcomProducts_ObjectIdentity=ObjectIdentity
ruggedcomProducts=_RuggedcomProducts_ObjectIdentity((1,3,6,1,4,1,15004,2))
if mibBuilder.loadTexts:ruggedcomProducts.setStatus(_A)
_RuggedcomRX1XXX_ObjectIdentity=ObjectIdentity
ruggedcomRX1XXX=_RuggedcomRX1XXX_ObjectIdentity((1,3,6,1,4,1,15004,2,4))
_RuggedcomRX1000_ObjectIdentity=ObjectIdentity
ruggedcomRX1000=_RuggedcomRX1000_ObjectIdentity((1,3,6,1,4,1,15004,2,4,1))
_RuggedcomRX1100_ObjectIdentity=ObjectIdentity
ruggedcomRX1100=_RuggedcomRX1100_ObjectIdentity((1,3,6,1,4,1,15004,2,4,2))
_RuggedcomRX5XXX_ObjectIdentity=ObjectIdentity
ruggedcomRX5XXX=_RuggedcomRX5XXX_ObjectIdentity((1,3,6,1,4,1,15004,2,5))
_RuggedcomRX5000_ObjectIdentity=ObjectIdentity
ruggedcomRX5000=_RuggedcomRX5000_ObjectIdentity((1,3,6,1,4,1,15004,2,5,1))
_RuggedcomMX5000_ObjectIdentity=ObjectIdentity
ruggedcomMX5000=_RuggedcomMX5000_ObjectIdentity((1,3,6,1,4,1,15004,2,5,2))
_RuggedmaxProducts_ObjectIdentity=ObjectIdentity
ruggedmaxProducts=_RuggedmaxProducts_ObjectIdentity((1,3,6,1,4,1,15004,2,6))
_RuggedcomRX15XX_ObjectIdentity=ObjectIdentity
ruggedcomRX15XX=_RuggedcomRX15XX_ObjectIdentity((1,3,6,1,4,1,15004,2,8))
_RuggedcomRX1500_ObjectIdentity=ObjectIdentity
ruggedcomRX1500=_RuggedcomRX1500_ObjectIdentity((1,3,6,1,4,1,15004,2,8,1))
_RuggedcomRX1501_ObjectIdentity=ObjectIdentity
ruggedcomRX1501=_RuggedcomRX1501_ObjectIdentity((1,3,6,1,4,1,15004,2,8,2))
_RuggedcomRX1510_ObjectIdentity=ObjectIdentity
ruggedcomRX1510=_RuggedcomRX1510_ObjectIdentity((1,3,6,1,4,1,15004,2,8,11))
_RuggedcomRX1511_ObjectIdentity=ObjectIdentity
ruggedcomRX1511=_RuggedcomRX1511_ObjectIdentity((1,3,6,1,4,1,15004,2,8,12))
_RuggedcomRX1512_ObjectIdentity=ObjectIdentity
ruggedcomRX1512=_RuggedcomRX1512_ObjectIdentity((1,3,6,1,4,1,15004,2,8,13))
_RuggedcomRX1XXXrox2X_ObjectIdentity=ObjectIdentity
ruggedcomRX1XXXrox2X=_RuggedcomRX1XXXrox2X_ObjectIdentity((1,3,6,1,4,1,15004,2,9))
_RuggedcomRX1000rox2X_ObjectIdentity=ObjectIdentity
ruggedcomRX1000rox2X=_RuggedcomRX1000rox2X_ObjectIdentity((1,3,6,1,4,1,15004,2,9,1))
_RuggedcomRX1100rox2X_ObjectIdentity=ObjectIdentity
ruggedcomRX1100rox2X=_RuggedcomRX1100rox2X_ObjectIdentity((1,3,6,1,4,1,15004,2,9,2))
_RuggedcomAirModule_ObjectIdentity=ObjectIdentity
ruggedcomAirModule=_RuggedcomAirModule_ObjectIdentity((1,3,6,1,4,1,15004,2,10))
_RuggedcomMC_ObjectIdentity=ObjectIdentity
ruggedcomMC=_RuggedcomMC_ObjectIdentity((1,3,6,1,4,1,15004,2,11))
_RuggedcomOtherEnterprises_ObjectIdentity=ObjectIdentity
ruggedcomOtherEnterprises=_RuggedcomOtherEnterprises_ObjectIdentity((1,3,6,1,4,1,15004,3))
if mibBuilder.loadTexts:ruggedcomOtherEnterprises.setStatus(_A)
_RuggedcomMgmt_ObjectIdentity=ObjectIdentity
ruggedcomMgmt=_RuggedcomMgmt_ObjectIdentity((1,3,6,1,4,1,15004,4))
if mibBuilder.loadTexts:ruggedcomMgmt.setStatus(_A)
_RuggedcomTraps_ObjectIdentity=ObjectIdentity
ruggedcomTraps=_RuggedcomTraps_ObjectIdentity((1,3,6,1,4,1,15004,5))
if mibBuilder.loadTexts:ruggedcomTraps.setStatus(_A)
_RuggedcomAgentCapabilities_ObjectIdentity=ObjectIdentity
ruggedcomAgentCapabilities=_RuggedcomAgentCapabilities_ObjectIdentity((1,3,6,1,4,1,15004,6))
if mibBuilder.loadTexts:ruggedcomAgentCapabilities.setStatus(_A)
_RuggedcomAgentCapability_ObjectIdentity=ObjectIdentity
ruggedcomAgentCapability=_RuggedcomAgentCapability_ObjectIdentity((1,3,6,1,4,1,15004,6,30))
if mibBuilder.loadTexts:ruggedcomAgentCapability.setStatus(_A)
mibBuilder.exportSymbols('RUGGEDCOM-MIB',**{'ruggedcom':ruggedcom,'ruggedcomExperiment':ruggedcomExperiment,'ruggedcomProducts':ruggedcomProducts,'ruggedcomRX1XXX':ruggedcomRX1XXX,'ruggedcomRX1000':ruggedcomRX1000,'ruggedcomRX1100':ruggedcomRX1100,'ruggedcomRX5XXX':ruggedcomRX5XXX,'ruggedcomRX5000':ruggedcomRX5000,'ruggedcomMX5000':ruggedcomMX5000,'ruggedmaxProducts':ruggedmaxProducts,'ruggedcomRX15XX':ruggedcomRX15XX,'ruggedcomRX1500':ruggedcomRX1500,'ruggedcomRX1501':ruggedcomRX1501,'ruggedcomRX1510':ruggedcomRX1510,'ruggedcomRX1511':ruggedcomRX1511,'ruggedcomRX1512':ruggedcomRX1512,'ruggedcomRX1XXXrox2X':ruggedcomRX1XXXrox2X,'ruggedcomRX1000rox2X':ruggedcomRX1000rox2X,'ruggedcomRX1100rox2X':ruggedcomRX1100rox2X,'ruggedcomAirModule':ruggedcomAirModule,'ruggedcomMC':ruggedcomMC,'ruggedcomOtherEnterprises':ruggedcomOtherEnterprises,'ruggedcomMgmt':ruggedcomMgmt,'ruggedcomTraps':ruggedcomTraps,'ruggedcomAgentCapabilities':ruggedcomAgentCapabilities,'ruggedcomAgentCapability':ruggedcomAgentCapability})