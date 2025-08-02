_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
waystream=ModuleIdentity((1,3,6,1,4,1,9303))
if mibBuilder.loadTexts:waystream.setRevisions(('2017-02-10 11:00','2011-01-11 18:01','2009-03-23 10:39','2008-01-17 14:05','2007-05-11 12:28'))
_WsProduct_ObjectIdentity=ObjectIdentity
wsProduct=_WsProduct_ObjectIdentity((1,3,6,1,4,1,9303,1))
if mibBuilder.loadTexts:wsProduct.setStatus(_A)
_WsConfig_ObjectIdentity=ObjectIdentity
wsConfig=_WsConfig_ObjectIdentity((1,3,6,1,4,1,9303,2))
if mibBuilder.loadTexts:wsConfig.setStatus(_A)
_IpdConfig_ObjectIdentity=ObjectIdentity
ipdConfig=_IpdConfig_ObjectIdentity((1,3,6,1,4,1,9303,2,1))
if mibBuilder.loadTexts:ipdConfig.setStatus(_A)
_WsExperiment_ObjectIdentity=ObjectIdentity
wsExperiment=_WsExperiment_ObjectIdentity((1,3,6,1,4,1,9303,3))
if mibBuilder.loadTexts:wsExperiment.setStatus(_A)
_WsMgmt_ObjectIdentity=ObjectIdentity
wsMgmt=_WsMgmt_ObjectIdentity((1,3,6,1,4,1,9303,4))
if mibBuilder.loadTexts:wsMgmt.setStatus(_A)
_WsModules_ObjectIdentity=ObjectIdentity
wsModules=_WsModules_ObjectIdentity((1,3,6,1,4,1,9303,5))
if mibBuilder.loadTexts:wsModules.setStatus(_A)
_PfSW_ObjectIdentity=ObjectIdentity
pfSW=_PfSW_ObjectIdentity((1,3,6,1,4,1,9303,6))
if mibBuilder.loadTexts:pfSW.setStatus(_A)
mibBuilder.exportSymbols('WAYSTREAM-SMI',**{'waystream':waystream,'wsProduct':wsProduct,'wsConfig':wsConfig,'ipdConfig':ipdConfig,'wsExperiment':wsExperiment,'wsMgmt':wsMgmt,'wsModules':wsModules,'pfSW':pfSW})