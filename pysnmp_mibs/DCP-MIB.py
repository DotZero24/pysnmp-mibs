_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
smartoptics,=mibBuilder.importSymbols('SO-MIB','smartoptics')
dcpGlobalModule=ModuleIdentity((1,3,6,1,4,1,30826,2,1,1,1))
if mibBuilder.loadTexts:dcpGlobalModule.setRevisions(('2018-10-08 14:44',))
_Dcp_ObjectIdentity=ObjectIdentity
dcp=_Dcp_ObjectIdentity((1,3,6,1,4,1,30826,2))
if mibBuilder.loadTexts:dcp.setStatus(_A)
_DcpReg_ObjectIdentity=ObjectIdentity
dcpReg=_DcpReg_ObjectIdentity((1,3,6,1,4,1,30826,2,1))
if mibBuilder.loadTexts:dcpReg.setStatus(_A)
_DcpModules_ObjectIdentity=ObjectIdentity
dcpModules=_DcpModules_ObjectIdentity((1,3,6,1,4,1,30826,2,1,1))
if mibBuilder.loadTexts:dcpModules.setStatus(_A)
_DcpGeneric_ObjectIdentity=ObjectIdentity
dcpGeneric=_DcpGeneric_ObjectIdentity((1,3,6,1,4,1,30826,2,2))
if mibBuilder.loadTexts:dcpGeneric.setStatus(_A)
_DcpProducts_ObjectIdentity=ObjectIdentity
dcpProducts=_DcpProducts_ObjectIdentity((1,3,6,1,4,1,30826,2,3))
if mibBuilder.loadTexts:dcpProducts.setStatus(_A)
_DcpCaps_ObjectIdentity=ObjectIdentity
dcpCaps=_DcpCaps_ObjectIdentity((1,3,6,1,4,1,30826,2,4))
if mibBuilder.loadTexts:dcpCaps.setStatus(_A)
_DcpReqs_ObjectIdentity=ObjectIdentity
dcpReqs=_DcpReqs_ObjectIdentity((1,3,6,1,4,1,30826,2,5))
if mibBuilder.loadTexts:dcpReqs.setStatus(_A)
_DcpExpr_ObjectIdentity=ObjectIdentity
dcpExpr=_DcpExpr_ObjectIdentity((1,3,6,1,4,1,30826,2,6))
if mibBuilder.loadTexts:dcpExpr.setStatus(_A)
mibBuilder.exportSymbols('DCP-MIB',**{'dcp':dcp,'dcpReg':dcpReg,'dcpModules':dcpModules,'dcpGlobalModule':dcpGlobalModule,'dcpGeneric':dcpGeneric,'dcpProducts':dcpProducts,'dcpCaps':dcpCaps,'dcpReqs':dcpReqs,'dcpExpr':dcpExpr})