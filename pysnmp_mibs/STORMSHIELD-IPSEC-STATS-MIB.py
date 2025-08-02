_B='current'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
stormshieldMIB,=mibBuilder.importSymbols('STORMSHIELD-SMI-MIB','stormshieldMIB')
snsIPSECStats=ModuleIdentity((1,3,6,1,4,1,11256,1,13))
if mibBuilder.loadTexts:snsIPSECStats.setRevisions(('2017-02-20 00:00',))
_SnsIPSECStatsSPD_ObjectIdentity=ObjectIdentity
snsIPSECStatsSPD=_SnsIPSECStatsSPD_ObjectIdentity((1,3,6,1,4,1,11256,1,13,1))
_SnsIPSECStatsSPDIn_Type=Counter64
_SnsIPSECStatsSPDIn_Object=MibScalar
snsIPSECStatsSPDIn=_SnsIPSECStatsSPDIn_Object((1,3,6,1,4,1,11256,1,13,1,1),_SnsIPSECStatsSPDIn_Type())
snsIPSECStatsSPDIn.setMaxAccess(_A)
if mibBuilder.loadTexts:snsIPSECStatsSPDIn.setStatus(_B)
_SnsIPSECStatsSPDOut_Type=Counter64
_SnsIPSECStatsSPDOut_Object=MibScalar
snsIPSECStatsSPDOut=_SnsIPSECStatsSPDOut_Object((1,3,6,1,4,1,11256,1,13,1,2),_SnsIPSECStatsSPDOut_Type())
snsIPSECStatsSPDOut.setMaxAccess(_A)
if mibBuilder.loadTexts:snsIPSECStatsSPDOut.setStatus(_B)
_SnsIPSECStatsSAD_ObjectIdentity=ObjectIdentity
snsIPSECStatsSAD=_SnsIPSECStatsSAD_ObjectIdentity((1,3,6,1,4,1,11256,1,13,2))
_SnsIPSECStatsSADLarval_Type=Counter64
_SnsIPSECStatsSADLarval_Object=MibScalar
snsIPSECStatsSADLarval=_SnsIPSECStatsSADLarval_Object((1,3,6,1,4,1,11256,1,13,2,1),_SnsIPSECStatsSADLarval_Type())
snsIPSECStatsSADLarval.setMaxAccess(_A)
if mibBuilder.loadTexts:snsIPSECStatsSADLarval.setStatus(_B)
_SnsIPSECStatsSADMature_Type=Counter64
_SnsIPSECStatsSADMature_Object=MibScalar
snsIPSECStatsSADMature=_SnsIPSECStatsSADMature_Object((1,3,6,1,4,1,11256,1,13,2,2),_SnsIPSECStatsSADMature_Type())
snsIPSECStatsSADMature.setMaxAccess(_A)
if mibBuilder.loadTexts:snsIPSECStatsSADMature.setStatus(_B)
_SnsIPSECStatsSADDying_Type=Counter64
_SnsIPSECStatsSADDying_Object=MibScalar
snsIPSECStatsSADDying=_SnsIPSECStatsSADDying_Object((1,3,6,1,4,1,11256,1,13,2,3),_SnsIPSECStatsSADDying_Type())
snsIPSECStatsSADDying.setMaxAccess(_A)
if mibBuilder.loadTexts:snsIPSECStatsSADDying.setStatus(_B)
_SnsIPSECStatsSADDead_Type=Counter64
_SnsIPSECStatsSADDead_Object=MibScalar
snsIPSECStatsSADDead=_SnsIPSECStatsSADDead_Object((1,3,6,1,4,1,11256,1,13,2,4),_SnsIPSECStatsSADDead_Type())
snsIPSECStatsSADDead.setMaxAccess(_A)
if mibBuilder.loadTexts:snsIPSECStatsSADDead.setStatus(_B)
mibBuilder.exportSymbols('STORMSHIELD-IPSEC-STATS-MIB',**{'snsIPSECStats':snsIPSECStats,'snsIPSECStatsSPD':snsIPSECStatsSPD,'snsIPSECStatsSPDIn':snsIPSECStatsSPDIn,'snsIPSECStatsSPDOut':snsIPSECStatsSPDOut,'snsIPSECStatsSAD':snsIPSECStatsSAD,'snsIPSECStatsSADLarval':snsIPSECStatsSADLarval,'snsIPSECStatsSADMature':snsIPSECStatsSADMature,'snsIPSECStatsSADDying':snsIPSECStatsSADDying,'snsIPSECStatsSADDead':snsIPSECStatsSADDead})