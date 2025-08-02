_E='read-only'
_D='rlSwPackageVersionName'
_C='RADLAN-SWPACKAGEVERSION-MIB'
_B='DisplayString'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rnd,=mibBuilder.importSymbols('RADLAN-MIB','rnd')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_B,'PhysAddress','TextualConvention')
rlSwPackageVersion=ModuleIdentity((1,3,6,1,4,1,89,67))
if mibBuilder.loadTexts:rlSwPackageVersion.setRevisions(('2007-01-02 00:00',))
_RlSwPackageVersionTable_Object=MibTable
rlSwPackageVersionTable=_RlSwPackageVersionTable_Object((1,3,6,1,4,1,89,67,1))
if mibBuilder.loadTexts:rlSwPackageVersionTable.setStatus(_A)
_RlSwPackageVersionEntry_Object=MibTableRow
rlSwPackageVersionEntry=_RlSwPackageVersionEntry_Object((1,3,6,1,4,1,89,67,1,1))
rlSwPackageVersionEntry.setIndexNames((1,_C,_D))
if mibBuilder.loadTexts:rlSwPackageVersionEntry.setStatus(_A)
class _RlSwPackageVersionName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_RlSwPackageVersionName_Type.__name__=_B
_RlSwPackageVersionName_Object=MibTableColumn
rlSwPackageVersionName=_RlSwPackageVersionName_Object((1,3,6,1,4,1,89,67,1,1,1),_RlSwPackageVersionName_Type())
rlSwPackageVersionName.setMaxAccess(_E)
if mibBuilder.loadTexts:rlSwPackageVersionName.setStatus(_A)
class _RlSwPackageVersionVesrion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_RlSwPackageVersionVesrion_Type.__name__=_B
_RlSwPackageVersionVesrion_Object=MibTableColumn
rlSwPackageVersionVesrion=_RlSwPackageVersionVesrion_Object((1,3,6,1,4,1,89,67,1,1,2),_RlSwPackageVersionVesrion_Type())
rlSwPackageVersionVesrion.setMaxAccess(_E)
if mibBuilder.loadTexts:rlSwPackageVersionVesrion.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'rlSwPackageVersion':rlSwPackageVersion,'rlSwPackageVersionTable':rlSwPackageVersionTable,'rlSwPackageVersionEntry':rlSwPackageVersionEntry,_D:rlSwPackageVersionName,'rlSwPackageVersionVesrion':rlSwPackageVersionVesrion})