_I='fsEgBspMIBGroup'
_H='fsEgBspInfoAge'
_G='fsEgBspMaxNumber'
_F='fsEgBspInfoPort'
_E='fsEgBspInfoVlanID'
_D='fsEgBspInfoMacAddress'
_C='read-only'
_B='current'
_A='FS-EG-BSP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
fsEgBspMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,147))
if mibBuilder.loadTexts:fsEgBspMIB.setRevisions(('2016-02-19 00:00',))
_FsEgBspMIBObjects_ObjectIdentity=ObjectIdentity
fsEgBspMIBObjects=_FsEgBspMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,147,1))
_FsEgBspMaxNumber_Type=Integer32
_FsEgBspMaxNumber_Object=MibScalar
fsEgBspMaxNumber=_FsEgBspMaxNumber_Object((1,3,6,1,4,1,52642,1,1,10,2,147,1,1),_FsEgBspMaxNumber_Type())
fsEgBspMaxNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:fsEgBspMaxNumber.setStatus(_B)
_FsEgBspInfoTable_Object=MibTable
fsEgBspInfoTable=_FsEgBspInfoTable_Object((1,3,6,1,4,1,52642,1,1,10,2,147,1,2))
if mibBuilder.loadTexts:fsEgBspInfoTable.setStatus(_B)
_FsEgBspInfoEntry_Object=MibTableRow
fsEgBspInfoEntry=_FsEgBspInfoEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,147,1,2,1))
fsEgBspInfoEntry.setIndexNames((0,_A,_D),(0,_A,_E),(0,_A,_F))
if mibBuilder.loadTexts:fsEgBspInfoEntry.setStatus(_B)
_FsEgBspInfoMacAddress_Type=MacAddress
_FsEgBspInfoMacAddress_Object=MibTableColumn
fsEgBspInfoMacAddress=_FsEgBspInfoMacAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,147,1,2,1,1),_FsEgBspInfoMacAddress_Type())
fsEgBspInfoMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsEgBspInfoMacAddress.setStatus(_B)
_FsEgBspInfoVlanID_Type=Integer32
_FsEgBspInfoVlanID_Object=MibTableColumn
fsEgBspInfoVlanID=_FsEgBspInfoVlanID_Object((1,3,6,1,4,1,52642,1,1,10,2,147,1,2,1,2),_FsEgBspInfoVlanID_Type())
fsEgBspInfoVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:fsEgBspInfoVlanID.setStatus(_B)
_FsEgBspInfoPort_Type=Integer32
_FsEgBspInfoPort_Object=MibTableColumn
fsEgBspInfoPort=_FsEgBspInfoPort_Object((1,3,6,1,4,1,52642,1,1,10,2,147,1,2,1,3),_FsEgBspInfoPort_Type())
fsEgBspInfoPort.setMaxAccess(_C)
if mibBuilder.loadTexts:fsEgBspInfoPort.setStatus(_B)
_FsEgBspInfoAge_Type=Integer32
_FsEgBspInfoAge_Object=MibTableColumn
fsEgBspInfoAge=_FsEgBspInfoAge_Object((1,3,6,1,4,1,52642,1,1,10,2,147,1,2,1,4),_FsEgBspInfoAge_Type())
fsEgBspInfoAge.setMaxAccess(_C)
if mibBuilder.loadTexts:fsEgBspInfoAge.setStatus(_B)
_FsEgBspMIBConformance_ObjectIdentity=ObjectIdentity
fsEgBspMIBConformance=_FsEgBspMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,147,2))
_FsEgBspMIBCompliances_ObjectIdentity=ObjectIdentity
fsEgBspMIBCompliances=_FsEgBspMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,147,2,1))
_FsEgBspMIBGroups_ObjectIdentity=ObjectIdentity
fsEgBspMIBGroups=_FsEgBspMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,147,2,2))
fsEgBspMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,147,2,2,1))
fsEgBspMIBGroup.setObjects(*((_A,_G),(_A,_D),(_A,_E),(_A,_F),(_A,_H)))
if mibBuilder.loadTexts:fsEgBspMIBGroup.setStatus(_B)
fsEgBspMIBCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,147,2,1,1))
fsEgBspMIBCompliance.setObjects((_A,_I))
if mibBuilder.loadTexts:fsEgBspMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'fsEgBspMIB':fsEgBspMIB,'fsEgBspMIBObjects':fsEgBspMIBObjects,_G:fsEgBspMaxNumber,'fsEgBspInfoTable':fsEgBspInfoTable,'fsEgBspInfoEntry':fsEgBspInfoEntry,_D:fsEgBspInfoMacAddress,_E:fsEgBspInfoVlanID,_F:fsEgBspInfoPort,_H:fsEgBspInfoAge,'fsEgBspMIBConformance':fsEgBspMIBConformance,'fsEgBspMIBCompliances':fsEgBspMIBCompliances,'fsEgBspMIBCompliance':fsEgBspMIBCompliance,'fsEgBspMIBGroups':fsEgBspMIBGroups,_I:fsEgBspMIBGroup})