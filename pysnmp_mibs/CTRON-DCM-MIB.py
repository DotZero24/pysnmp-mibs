if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ctDcm,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctDcm')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_DCM_ObjectIdentity=ObjectIdentity
dCM=_DCM_ObjectIdentity((1,3,6,1,4,1,52,4,1,6,1))
_DCMMode_Type=Integer32
_DCMMode_Object=MibScalar
dCMMode=_DCMMode_Object((1,3,6,1,4,1,52,4,1,6,1,1),_DCMMode_Type())
dCMMode.setMaxAccess('read-write')
if mibBuilder.loadTexts:dCMMode.setStatus('mandatory')
mibBuilder.exportSymbols('CTRON-DCM-MIB',**{'dCM':dCM,'dCMMode':dCMMode})