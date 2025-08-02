_H='rbnFastVrrpObjectGroup'
_G='rbnFastVrrpOperAdvertisementInterval'
_F='rbnFastVrrpOperVrId'
_E='Integer32'
_D='ifIndex'
_C='IF-MIB'
_B='RBN-FAST-VRRP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_C,_D)
rbnMgmt,=mibBuilder.importSymbols('RBN-SMI','rbnMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
VrId,=mibBuilder.importSymbols('VRRP-MIB','VrId')
rbnFastVrrpMIB=ModuleIdentity((1,3,6,1,4,1,2352,2,45))
if mibBuilder.loadTexts:rbnFastVrrpMIB.setRevisions(('2008-05-21 00:00',))
_RbnFastVrrpMIBObjects_ObjectIdentity=ObjectIdentity
rbnFastVrrpMIBObjects=_RbnFastVrrpMIBObjects_ObjectIdentity((1,3,6,1,4,1,2352,2,45,1))
_RbnFastVrrpOperTable_Object=MibTable
rbnFastVrrpOperTable=_RbnFastVrrpOperTable_Object((1,3,6,1,4,1,2352,2,45,1,1))
if mibBuilder.loadTexts:rbnFastVrrpOperTable.setStatus(_A)
_RbnFastVrrpOperEntry_Object=MibTableRow
rbnFastVrrpOperEntry=_RbnFastVrrpOperEntry_Object((1,3,6,1,4,1,2352,2,45,1,1,1))
rbnFastVrrpOperEntry.setIndexNames((0,_C,_D),(0,_B,_F))
if mibBuilder.loadTexts:rbnFastVrrpOperEntry.setStatus(_A)
_RbnFastVrrpOperVrId_Type=VrId
_RbnFastVrrpOperVrId_Object=MibTableColumn
rbnFastVrrpOperVrId=_RbnFastVrrpOperVrId_Object((1,3,6,1,4,1,2352,2,45,1,1,1,1),_RbnFastVrrpOperVrId_Type())
rbnFastVrrpOperVrId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:rbnFastVrrpOperVrId.setStatus(_A)
class _RbnFastVrrpOperAdvertisementInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,999))
_RbnFastVrrpOperAdvertisementInterval_Type.__name__=_E
_RbnFastVrrpOperAdvertisementInterval_Object=MibTableColumn
rbnFastVrrpOperAdvertisementInterval=_RbnFastVrrpOperAdvertisementInterval_Object((1,3,6,1,4,1,2352,2,45,1,1,1,2),_RbnFastVrrpOperAdvertisementInterval_Type())
rbnFastVrrpOperAdvertisementInterval.setMaxAccess('read-only')
if mibBuilder.loadTexts:rbnFastVrrpOperAdvertisementInterval.setStatus(_A)
if mibBuilder.loadTexts:rbnFastVrrpOperAdvertisementInterval.setUnits('milliseconds')
_RbnFastVrrpConformance_ObjectIdentity=ObjectIdentity
rbnFastVrrpConformance=_RbnFastVrrpConformance_ObjectIdentity((1,3,6,1,4,1,2352,2,45,2))
_RbnFastVrrpMIBCompliances_ObjectIdentity=ObjectIdentity
rbnFastVrrpMIBCompliances=_RbnFastVrrpMIBCompliances_ObjectIdentity((1,3,6,1,4,1,2352,2,45,2,1))
_RbnFastVrrpMIBGroups_ObjectIdentity=ObjectIdentity
rbnFastVrrpMIBGroups=_RbnFastVrrpMIBGroups_ObjectIdentity((1,3,6,1,4,1,2352,2,45,2,2))
rbnFastVrrpObjectGroup=ObjectGroup((1,3,6,1,4,1,2352,2,45,2,2,1))
rbnFastVrrpObjectGroup.setObjects((_B,_G))
if mibBuilder.loadTexts:rbnFastVrrpObjectGroup.setStatus(_A)
rbnFastVrrpCompliance=ModuleCompliance((1,3,6,1,4,1,2352,2,45,2,1,1))
rbnFastVrrpCompliance.setObjects((_B,_H))
if mibBuilder.loadTexts:rbnFastVrrpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'rbnFastVrrpMIB':rbnFastVrrpMIB,'rbnFastVrrpMIBObjects':rbnFastVrrpMIBObjects,'rbnFastVrrpOperTable':rbnFastVrrpOperTable,'rbnFastVrrpOperEntry':rbnFastVrrpOperEntry,_F:rbnFastVrrpOperVrId,_G:rbnFastVrrpOperAdvertisementInterval,'rbnFastVrrpConformance':rbnFastVrrpConformance,'rbnFastVrrpMIBCompliances':rbnFastVrrpMIBCompliances,'rbnFastVrrpCompliance':rbnFastVrrpCompliance,'rbnFastVrrpMIBGroups':rbnFastVrrpMIBGroups,_H:rbnFastVrrpObjectGroup})