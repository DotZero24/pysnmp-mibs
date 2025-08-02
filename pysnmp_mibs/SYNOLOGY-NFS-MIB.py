_M='nfsGroup'
_L='nfsWriteOPS'
_K='nfsReadOPS'
_J='nfsTotalOPS'
_I='nfsWriteMaxLatency'
_H='nfsReadMaxLatency'
_G='nfsTotalMaxLatency'
_F='nfsName'
_E='nfsIndex'
_D='Integer32'
_C='read-only'
_B='SYNOLOGY-NFS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
nfs=ModuleIdentity((1,3,6,1,4,1,6574,107))
if mibBuilder.loadTexts:nfs.setRevisions(('2018-08-10 00:00',))
_Synology_ObjectIdentity=ObjectIdentity
synology=_Synology_ObjectIdentity((1,3,6,1,4,1,6574))
_NfsTable_Object=MibTable
nfsTable=_NfsTable_Object((1,3,6,1,4,1,6574,107,1))
if mibBuilder.loadTexts:nfsTable.setStatus(_A)
_NfsEntry_Object=MibTableRow
nfsEntry=_NfsEntry_Object((1,3,6,1,4,1,6574,107,1,1))
nfsEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:nfsEntry.setStatus(_A)
class _NfsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NfsIndex_Type.__name__=_D
_NfsIndex_Object=MibTableColumn
nfsIndex=_NfsIndex_Object((1,3,6,1,4,1,6574,107,1,1,1),_NfsIndex_Type())
nfsIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:nfsIndex.setStatus(_A)
_NfsName_Type=DisplayString
_NfsName_Object=MibTableColumn
nfsName=_NfsName_Object((1,3,6,1,4,1,6574,107,1,1,2),_NfsName_Type())
nfsName.setMaxAccess(_C)
if mibBuilder.loadTexts:nfsName.setStatus(_A)
_NfsTotalMaxLatency_Type=Integer32
_NfsTotalMaxLatency_Object=MibTableColumn
nfsTotalMaxLatency=_NfsTotalMaxLatency_Object((1,3,6,1,4,1,6574,107,1,1,3),_NfsTotalMaxLatency_Type())
nfsTotalMaxLatency.setMaxAccess(_C)
if mibBuilder.loadTexts:nfsTotalMaxLatency.setStatus(_A)
_NfsReadMaxLatency_Type=Integer32
_NfsReadMaxLatency_Object=MibTableColumn
nfsReadMaxLatency=_NfsReadMaxLatency_Object((1,3,6,1,4,1,6574,107,1,1,4),_NfsReadMaxLatency_Type())
nfsReadMaxLatency.setMaxAccess(_C)
if mibBuilder.loadTexts:nfsReadMaxLatency.setStatus(_A)
_NfsWriteMaxLatency_Type=Integer32
_NfsWriteMaxLatency_Object=MibTableColumn
nfsWriteMaxLatency=_NfsWriteMaxLatency_Object((1,3,6,1,4,1,6574,107,1,1,5),_NfsWriteMaxLatency_Type())
nfsWriteMaxLatency.setMaxAccess(_C)
if mibBuilder.loadTexts:nfsWriteMaxLatency.setStatus(_A)
_NfsTotalOPS_Type=Counter64
_NfsTotalOPS_Object=MibTableColumn
nfsTotalOPS=_NfsTotalOPS_Object((1,3,6,1,4,1,6574,107,1,1,6),_NfsTotalOPS_Type())
nfsTotalOPS.setMaxAccess(_C)
if mibBuilder.loadTexts:nfsTotalOPS.setStatus(_A)
_NfsReadOPS_Type=Counter64
_NfsReadOPS_Object=MibTableColumn
nfsReadOPS=_NfsReadOPS_Object((1,3,6,1,4,1,6574,107,1,1,7),_NfsReadOPS_Type())
nfsReadOPS.setMaxAccess(_C)
if mibBuilder.loadTexts:nfsReadOPS.setStatus(_A)
_NfsWriteOPS_Type=Counter64
_NfsWriteOPS_Object=MibTableColumn
nfsWriteOPS=_NfsWriteOPS_Object((1,3,6,1,4,1,6574,107,1,1,8),_NfsWriteOPS_Type())
nfsWriteOPS.setMaxAccess(_C)
if mibBuilder.loadTexts:nfsWriteOPS.setStatus(_A)
_NfsConformance_ObjectIdentity=ObjectIdentity
nfsConformance=_NfsConformance_ObjectIdentity((1,3,6,1,4,1,6574,107,2))
_NfsCompliances_ObjectIdentity=ObjectIdentity
nfsCompliances=_NfsCompliances_ObjectIdentity((1,3,6,1,4,1,6574,107,2,1))
_NfsGroups_ObjectIdentity=ObjectIdentity
nfsGroups=_NfsGroups_ObjectIdentity((1,3,6,1,4,1,6574,107,2,2))
nfsGroup=ObjectGroup((1,3,6,1,4,1,6574,107,2,2,1))
nfsGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:nfsGroup.setStatus(_A)
nfsCompliance=ModuleCompliance((1,3,6,1,4,1,6574,107,2,1,1))
nfsCompliance.setObjects((_B,_M))
if mibBuilder.loadTexts:nfsCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'synology':synology,'nfs':nfs,'nfsTable':nfsTable,'nfsEntry':nfsEntry,_E:nfsIndex,_F:nfsName,_G:nfsTotalMaxLatency,_H:nfsReadMaxLatency,_I:nfsWriteMaxLatency,_J:nfsTotalOPS,_K:nfsReadOPS,_L:nfsWriteOPS,'nfsConformance':nfsConformance,'nfsCompliances':nfsCompliances,'nfsCompliance':nfsCompliance,'nfsGroups':nfsGroups,_M:nfsGroup})