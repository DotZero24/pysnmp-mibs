_E='sipDebugGroupVer1'
_D='sipDebugContextSnapshotTime'
_C='Unsigned32'
_B='MX-SIP-DEBUG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mediatrixExperimental,=mibBuilder.importSymbols('MX-SMI','mediatrixExperimental')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
sipDebugMIB=ModuleIdentity((1,3,6,1,4,1,4935,99,23))
if mibBuilder.loadTexts:sipDebugMIB.setRevisions(('1903-11-13 00:00',))
_SipDebugMIBObjects_ObjectIdentity=ObjectIdentity
sipDebugMIBObjects=_SipDebugMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,99,23,1))
class _SipDebugContextSnapshotTime_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10080))
_SipDebugContextSnapshotTime_Type.__name__=_C
_SipDebugContextSnapshotTime_Object=MibScalar
sipDebugContextSnapshotTime=_SipDebugContextSnapshotTime_Object((1,3,6,1,4,1,4935,99,23,1,5),_SipDebugContextSnapshotTime_Type())
sipDebugContextSnapshotTime.setMaxAccess('read-write')
if mibBuilder.loadTexts:sipDebugContextSnapshotTime.setStatus(_A)
_SipDebugConformance_ObjectIdentity=ObjectIdentity
sipDebugConformance=_SipDebugConformance_ObjectIdentity((1,3,6,1,4,1,4935,99,23,2))
_SipDebugCompliances_ObjectIdentity=ObjectIdentity
sipDebugCompliances=_SipDebugCompliances_ObjectIdentity((1,3,6,1,4,1,4935,99,23,2,1))
_SipDebugGroups_ObjectIdentity=ObjectIdentity
sipDebugGroups=_SipDebugGroups_ObjectIdentity((1,3,6,1,4,1,4935,99,23,2,2))
sipDebugGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,99,23,2,2,5))
sipDebugGroupVer1.setObjects((_B,_D))
if mibBuilder.loadTexts:sipDebugGroupVer1.setStatus(_A)
sipDebugBasicComplVer1=ModuleCompliance((1,3,6,1,4,1,4935,99,23,2,1,1))
sipDebugBasicComplVer1.setObjects((_B,_E))
if mibBuilder.loadTexts:sipDebugBasicComplVer1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'sipDebugMIB':sipDebugMIB,'sipDebugMIBObjects':sipDebugMIBObjects,_D:sipDebugContextSnapshotTime,'sipDebugConformance':sipDebugConformance,'sipDebugCompliances':sipDebugCompliances,'sipDebugBasicComplVer1':sipDebugBasicComplVer1,'sipDebugGroups':sipDebugGroups,_E:sipDebugGroupVer1})