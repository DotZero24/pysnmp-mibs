_G='tnMirrorDestinationExtnEntry'
_F='tnMirrorSourcePortExtnEntry'
_E='TProfileOrNone'
_D='TN-SAS-MIRROR-MIB'
_C='read-create'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tnMirrorDestinationEntry,tnMirrorSourcePortEntry=mibBuilder.importSymbols('TN-MIRROR-MIB','tnMirrorDestinationEntry','tnMirrorSourcePortEntry')
TProfileOrNone,=mibBuilder.importSymbols('TN-TC-MIB',_E)
tnSASModules,tnSASObjs,tnSRMIBModules,tnSRNotifyPrefix,tnSRObjs=mibBuilder.importSymbols('TROPIC-GLOBAL-REG','tnSASModules','tnSASObjs','tnSRMIBModules','tnSRNotifyPrefix','tnSRObjs')
tnSASMirrorMIBModule=ModuleIdentity((1,3,6,1,4,1,7483,7,2,1,1,13))
if mibBuilder.loadTexts:tnSASMirrorMIBModule.setRevisions(('2011-05-01 00:00',))
_TnSASMirrorObjects_ObjectIdentity=ObjectIdentity
tnSASMirrorObjects=_TnSASMirrorObjects_ObjectIdentity((1,3,6,1,4,1,7483,7,2,2,2,13))
_TnMirrorSourcePortExtnTable_Object=MibTable
tnMirrorSourcePortExtnTable=_TnMirrorSourcePortExtnTable_Object((1,3,6,1,4,1,7483,7,2,2,2,13,1))
if mibBuilder.loadTexts:tnMirrorSourcePortExtnTable.setStatus(_A)
_TnMirrorSourcePortExtnEntry_Object=MibTableRow
tnMirrorSourcePortExtnEntry=_TnMirrorSourcePortExtnEntry_Object((1,3,6,1,4,1,7483,7,2,2,2,13,1,1))
if mibBuilder.loadTexts:tnMirrorSourcePortExtnEntry.setStatus(_A)
class _TnMirrorSourcePortEgressMirroringType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true-egress-mirroring',1),('normal-egress-mirroring',2)))
_TnMirrorSourcePortEgressMirroringType_Type.__name__=_B
_TnMirrorSourcePortEgressMirroringType_Object=MibTableColumn
tnMirrorSourcePortEgressMirroringType=_TnMirrorSourcePortEgressMirroringType_Object((1,3,6,1,4,1,7483,7,2,2,2,13,1,1,1),_TnMirrorSourcePortEgressMirroringType_Type())
tnMirrorSourcePortEgressMirroringType.setMaxAccess(_C)
if mibBuilder.loadTexts:tnMirrorSourcePortEgressMirroringType.setStatus(_A)
_TnMirrorDestinationExtnTable_Object=MibTable
tnMirrorDestinationExtnTable=_TnMirrorDestinationExtnTable_Object((1,3,6,1,4,1,7483,7,2,2,2,13,2))
if mibBuilder.loadTexts:tnMirrorDestinationExtnTable.setStatus(_A)
_TnMirrorDestinationExtnEntry_Object=MibTableRow
tnMirrorDestinationExtnEntry=_TnMirrorDestinationExtnEntry_Object((1,3,6,1,4,1,7483,7,2,2,2,13,2,1))
if mibBuilder.loadTexts:tnMirrorDestinationExtnEntry.setStatus(_A)
class _TnMirrorDestinationFCProfile_Type(TProfileOrNone):defaultValue=2
_TnMirrorDestinationFCProfile_Type.__name__=_E
_TnMirrorDestinationFCProfile_Object=MibTableColumn
tnMirrorDestinationFCProfile=_TnMirrorDestinationFCProfile_Object((1,3,6,1,4,1,7483,7,2,2,2,13,2,1,1),_TnMirrorDestinationFCProfile_Type())
tnMirrorDestinationFCProfile.setMaxAccess(_C)
if mibBuilder.loadTexts:tnMirrorDestinationFCProfile.setStatus(_A)
class _TnMirrorDestinationMirrorSourceType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('local',1),('remote',2),('both',3)))
_TnMirrorDestinationMirrorSourceType_Type.__name__=_B
_TnMirrorDestinationMirrorSourceType_Object=MibTableColumn
tnMirrorDestinationMirrorSourceType=_TnMirrorDestinationMirrorSourceType_Object((1,3,6,1,4,1,7483,7,2,2,2,13,2,1,2),_TnMirrorDestinationMirrorSourceType_Type())
tnMirrorDestinationMirrorSourceType.setMaxAccess(_C)
if mibBuilder.loadTexts:tnMirrorDestinationMirrorSourceType.setStatus(_A)
tnMirrorSourcePortEntry.registerAugmentions((_D,_F))
tnMirrorSourcePortExtnEntry.setIndexNames(*tnMirrorSourcePortEntry.getIndexNames())
tnMirrorDestinationEntry.registerAugmentions((_D,_G))
tnMirrorDestinationExtnEntry.setIndexNames(*tnMirrorDestinationEntry.getIndexNames())
mibBuilder.exportSymbols(_D,**{'tnSASMirrorMIBModule':tnSASMirrorMIBModule,'tnSASMirrorObjects':tnSASMirrorObjects,'tnMirrorSourcePortExtnTable':tnMirrorSourcePortExtnTable,_F:tnMirrorSourcePortExtnEntry,'tnMirrorSourcePortEgressMirroringType':tnMirrorSourcePortEgressMirroringType,'tnMirrorDestinationExtnTable':tnMirrorDestinationExtnTable,_G:tnMirrorDestinationExtnEntry,'tnMirrorDestinationFCProfile':tnMirrorDestinationFCProfile,'tnMirrorDestinationMirrorSourceType':tnMirrorDestinationMirrorSourceType})