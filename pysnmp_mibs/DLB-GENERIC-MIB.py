_C='current'
_B='sysLocation'
_A='SNMPv2-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlbMgmt,=mibBuilder.importSymbols('DELIBERANT-MIB','dlbMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysLocation,=mibBuilder.importSymbols(_A,_B)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
dlbGenericMIB=ModuleIdentity((1,3,6,1,4,1,32761,3,1))
if mibBuilder.loadTexts:dlbGenericMIB.setRevisions(('2009-02-13 00:00',))
_DlbGenericMIBObjects_ObjectIdentity=ObjectIdentity
dlbGenericMIBObjects=_DlbGenericMIBObjects_ObjectIdentity((1,3,6,1,4,1,32761,3,1,1))
_DlbGenericNotifs_ObjectIdentity=ObjectIdentity
dlbGenericNotifs=_DlbGenericNotifs_ObjectIdentity((1,3,6,1,4,1,32761,3,1,1,0))
_DlbGenericInfo_ObjectIdentity=ObjectIdentity
dlbGenericInfo=_DlbGenericInfo_ObjectIdentity((1,3,6,1,4,1,32761,3,1,1,1))
dlbPowerLoss=NotificationType((1,3,6,1,4,1,32761,3,1,1,0,1))
dlbPowerLoss.setObjects((_A,_B))
if mibBuilder.loadTexts:dlbPowerLoss.setStatus(_C)
dlbAdministrativeReboot=NotificationType((1,3,6,1,4,1,32761,3,1,1,0,2))
dlbAdministrativeReboot.setObjects((_A,_B))
if mibBuilder.loadTexts:dlbAdministrativeReboot.setStatus(_C)
mibBuilder.exportSymbols('DLB-GENERIC-MIB',**{'dlbGenericMIB':dlbGenericMIB,'dlbGenericMIBObjects':dlbGenericMIBObjects,'dlbGenericNotifs':dlbGenericNotifs,'dlbPowerLoss':dlbPowerLoss,'dlbAdministrativeReboot':dlbAdministrativeReboot,'dlbGenericInfo':dlbGenericInfo})