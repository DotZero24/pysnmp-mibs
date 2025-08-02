_B='current'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
h3cL2tp=ModuleIdentity((1,3,6,1,4,1,2011,10,2,139))
if mibBuilder.loadTexts:h3cL2tp.setRevisions(('2013-07-05 15:18',))
_H3cL2tpObjects_ObjectIdentity=ObjectIdentity
h3cL2tpObjects=_H3cL2tpObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,139,1))
_H3cL2tpScalar_ObjectIdentity=ObjectIdentity
h3cL2tpScalar=_H3cL2tpScalar_ObjectIdentity((1,3,6,1,4,1,2011,10,2,139,1,1))
_H3cL2tpStats_ObjectIdentity=ObjectIdentity
h3cL2tpStats=_H3cL2tpStats_ObjectIdentity((1,3,6,1,4,1,2011,10,2,139,1,1,1))
_H3cL2tpStatsTotalTunnels_Type=Counter32
_H3cL2tpStatsTotalTunnels_Object=MibScalar
h3cL2tpStatsTotalTunnels=_H3cL2tpStatsTotalTunnels_Object((1,3,6,1,4,1,2011,10,2,139,1,1,1,1),_H3cL2tpStatsTotalTunnels_Type())
h3cL2tpStatsTotalTunnels.setMaxAccess(_A)
if mibBuilder.loadTexts:h3cL2tpStatsTotalTunnels.setStatus(_B)
_H3cL2tpStatsTotalSessions_Type=Counter32
_H3cL2tpStatsTotalSessions_Object=MibScalar
h3cL2tpStatsTotalSessions=_H3cL2tpStatsTotalSessions_Object((1,3,6,1,4,1,2011,10,2,139,1,1,1,2),_H3cL2tpStatsTotalSessions_Type())
h3cL2tpStatsTotalSessions.setMaxAccess(_A)
if mibBuilder.loadTexts:h3cL2tpStatsTotalSessions.setStatus(_B)
_H3cL2tpSessionRate_Type=Integer32
_H3cL2tpSessionRate_Object=MibScalar
h3cL2tpSessionRate=_H3cL2tpSessionRate_Object((1,3,6,1,4,1,2011,10,2,139,1,1,1,3),_H3cL2tpSessionRate_Type())
h3cL2tpSessionRate.setMaxAccess(_A)
if mibBuilder.loadTexts:h3cL2tpSessionRate.setStatus(_B)
mibBuilder.exportSymbols('H3C-L2TP-MIB',**{'h3cL2tp':h3cL2tp,'h3cL2tpObjects':h3cL2tpObjects,'h3cL2tpScalar':h3cL2tpScalar,'h3cL2tpStats':h3cL2tpStats,'h3cL2tpStatsTotalTunnels':h3cL2tpStatsTotalTunnels,'h3cL2tpStatsTotalSessions':h3cL2tpStatsTotalSessions,'h3cL2tpSessionRate':h3cL2tpSessionRate})