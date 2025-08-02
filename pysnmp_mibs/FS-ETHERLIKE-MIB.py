_F='fscollisionMIBGroups'
_E='fsLocIfCollisions'
_D='read-only'
_C='fsEtherlikeIfIndex'
_B='FS-ETHERLIKE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
IfIndex,=mibBuilder.importSymbols('FS-TC','IfIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
fsEtherlikeMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,55))
if mibBuilder.loadTexts:fsEtherlikeMIB.setRevisions(('2009-09-17 00:00',))
_FsEtherlikeMIBObjects_ObjectIdentity=ObjectIdentity
fsEtherlikeMIBObjects=_FsEtherlikeMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,55,1))
_FsEtherlikeTable_Object=MibTable
fsEtherlikeTable=_FsEtherlikeTable_Object((1,3,6,1,4,1,52642,1,1,10,2,55,1,1))
if mibBuilder.loadTexts:fsEtherlikeTable.setStatus(_A)
_FsEtherlikeEntry_Object=MibTableRow
fsEtherlikeEntry=_FsEtherlikeEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,55,1,1,1))
fsEtherlikeEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:fsEtherlikeEntry.setStatus(_A)
_FsEtherlikeIfIndex_Type=IfIndex
_FsEtherlikeIfIndex_Object=MibTableColumn
fsEtherlikeIfIndex=_FsEtherlikeIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,55,1,1,1,1),_FsEtherlikeIfIndex_Type())
fsEtherlikeIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsEtherlikeIfIndex.setStatus(_A)
_FsLocIfCollisions_Type=Counter64
_FsLocIfCollisions_Object=MibTableColumn
fsLocIfCollisions=_FsLocIfCollisions_Object((1,3,6,1,4,1,52642,1,1,10,2,55,1,1,1,2),_FsLocIfCollisions_Type())
fsLocIfCollisions.setMaxAccess(_D)
if mibBuilder.loadTexts:fsLocIfCollisions.setStatus(_A)
_FsEtherlikeMIBConformance_ObjectIdentity=ObjectIdentity
fsEtherlikeMIBConformance=_FsEtherlikeMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,55,3))
_FsEtherlikeMIBCompliances_ObjectIdentity=ObjectIdentity
fsEtherlikeMIBCompliances=_FsEtherlikeMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,55,3,1))
_FsEtherlikeMIBGroups_ObjectIdentity=ObjectIdentity
fsEtherlikeMIBGroups=_FsEtherlikeMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,55,3,2))
fscollisionMIBGroups=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,55,3,2,1))
fscollisionMIBGroups.setObjects(*((_B,_C),(_B,_E)))
if mibBuilder.loadTexts:fscollisionMIBGroups.setStatus(_A)
fsEtherlikeMIBCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,55,3,1,1))
fsEtherlikeMIBCompliance.setObjects((_B,_F))
if mibBuilder.loadTexts:fsEtherlikeMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fsEtherlikeMIB':fsEtherlikeMIB,'fsEtherlikeMIBObjects':fsEtherlikeMIBObjects,'fsEtherlikeTable':fsEtherlikeTable,'fsEtherlikeEntry':fsEtherlikeEntry,_C:fsEtherlikeIfIndex,_E:fsLocIfCollisions,'fsEtherlikeMIBConformance':fsEtherlikeMIBConformance,'fsEtherlikeMIBCompliances':fsEtherlikeMIBCompliances,'fsEtherlikeMIBCompliance':fsEtherlikeMIBCompliance,'fsEtherlikeMIBGroups':fsEtherlikeMIBGroups,_F:fscollisionMIBGroups})