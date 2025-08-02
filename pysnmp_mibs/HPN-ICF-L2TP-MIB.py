_B='current'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpnicfL2tp=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,139))
if mibBuilder.loadTexts:hpnicfL2tp.setRevisions(('2013-07-05 15:18',))
_HpnicfL2tpObjects_ObjectIdentity=ObjectIdentity
hpnicfL2tpObjects=_HpnicfL2tpObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,139,1))
_HpnicfL2tpScalar_ObjectIdentity=ObjectIdentity
hpnicfL2tpScalar=_HpnicfL2tpScalar_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,139,1,1))
_HpnicfL2tpStats_ObjectIdentity=ObjectIdentity
hpnicfL2tpStats=_HpnicfL2tpStats_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,139,1,1,1))
_HpnicfL2tpStatsTotalTunnels_Type=Counter32
_HpnicfL2tpStatsTotalTunnels_Object=MibScalar
hpnicfL2tpStatsTotalTunnels=_HpnicfL2tpStatsTotalTunnels_Object((1,3,6,1,4,1,11,2,14,11,15,2,139,1,1,1,1),_HpnicfL2tpStatsTotalTunnels_Type())
hpnicfL2tpStatsTotalTunnels.setMaxAccess(_A)
if mibBuilder.loadTexts:hpnicfL2tpStatsTotalTunnels.setStatus(_B)
_HpnicfL2tpStatsTotalSessions_Type=Counter32
_HpnicfL2tpStatsTotalSessions_Object=MibScalar
hpnicfL2tpStatsTotalSessions=_HpnicfL2tpStatsTotalSessions_Object((1,3,6,1,4,1,11,2,14,11,15,2,139,1,1,1,2),_HpnicfL2tpStatsTotalSessions_Type())
hpnicfL2tpStatsTotalSessions.setMaxAccess(_A)
if mibBuilder.loadTexts:hpnicfL2tpStatsTotalSessions.setStatus(_B)
_HpnicfL2tpSessionRate_Type=Integer32
_HpnicfL2tpSessionRate_Object=MibScalar
hpnicfL2tpSessionRate=_HpnicfL2tpSessionRate_Object((1,3,6,1,4,1,11,2,14,11,15,2,139,1,1,1,3),_HpnicfL2tpSessionRate_Type())
hpnicfL2tpSessionRate.setMaxAccess(_A)
if mibBuilder.loadTexts:hpnicfL2tpSessionRate.setStatus(_B)
mibBuilder.exportSymbols('HPN-ICF-L2TP-MIB',**{'hpnicfL2tp':hpnicfL2tp,'hpnicfL2tpObjects':hpnicfL2tpObjects,'hpnicfL2tpScalar':hpnicfL2tpScalar,'hpnicfL2tpStats':hpnicfL2tpStats,'hpnicfL2tpStatsTotalTunnels':hpnicfL2tpStatsTotalTunnels,'hpnicfL2tpStatsTotalSessions':hpnicfL2tpStatsTotalSessions,'hpnicfL2tpSessionRate':hpnicfL2tpSessionRate})