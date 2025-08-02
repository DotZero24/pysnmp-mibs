if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adIdentityShared,adShared=mibBuilder.importSymbols('ADTRAN-MIB','adIdentityShared','adShared')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adShdslIdentity=ModuleIdentity((1,3,6,1,4,1,664,6,10000,59))
if mibBuilder.loadTexts:adShdslIdentity.setRevisions(('2007-04-06 00:00',))
_AdSHDSL_ObjectIdentity=ObjectIdentity
adSHDSL=_AdSHDSL_ObjectIdentity((1,3,6,1,4,1,664,5,59))
_AdGenEShdsl_ObjectIdentity=ObjectIdentity
adGenEShdsl=_AdGenEShdsl_ObjectIdentity((1,3,6,1,4,1,664,5,59,1))
_AdGenDslProxy_ObjectIdentity=ObjectIdentity
adGenDslProxy=_AdGenDslProxy_ObjectIdentity((1,3,6,1,4,1,664,5,59,4))
_AdGenEShdslID_ObjectIdentity=ObjectIdentity
adGenEShdslID=_AdGenEShdslID_ObjectIdentity((1,3,6,1,4,1,664,6,10000,59,1))
_AdGenDslProxyID_ObjectIdentity=ObjectIdentity
adGenDslProxyID=_AdGenDslProxyID_ObjectIdentity((1,3,6,1,4,1,664,6,10000,59,4))
mibBuilder.exportSymbols('ADTRAN-SHARED-SHDSL-MIB',**{'adSHDSL':adSHDSL,'adGenEShdsl':adGenEShdsl,'adGenDslProxy':adGenDslProxy,'adShdslIdentity':adShdslIdentity,'adGenEShdslID':adGenEShdslID,'adGenDslProxyID':adGenDslProxyID})