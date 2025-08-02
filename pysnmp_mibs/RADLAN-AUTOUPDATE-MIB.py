_B='current'
_A='read-write'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rnd,=mibBuilder.importSymbols('RADLAN-MIB','rnd')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
rlAutoUpdate=ModuleIdentity((1,3,6,1,4,1,89,123))
_RlAutoUpdateEnable_Type=TruthValue
_RlAutoUpdateEnable_Object=MibScalar
rlAutoUpdateEnable=_RlAutoUpdateEnable_Object((1,3,6,1,4,1,89,123,1),_RlAutoUpdateEnable_Type())
rlAutoUpdateEnable.setMaxAccess(_A)
if mibBuilder.loadTexts:rlAutoUpdateEnable.setStatus(_B)
_RlAutoUpdateFilesBoot_Type=TruthValue
_RlAutoUpdateFilesBoot_Object=MibScalar
rlAutoUpdateFilesBoot=_RlAutoUpdateFilesBoot_Object((1,3,6,1,4,1,89,123,2),_RlAutoUpdateFilesBoot_Type())
rlAutoUpdateFilesBoot.setMaxAccess(_A)
if mibBuilder.loadTexts:rlAutoUpdateFilesBoot.setStatus(_B)
_RlAutoUpdateFilesImage_Type=TruthValue
_RlAutoUpdateFilesImage_Object=MibScalar
rlAutoUpdateFilesImage=_RlAutoUpdateFilesImage_Object((1,3,6,1,4,1,89,123,3),_RlAutoUpdateFilesImage_Type())
rlAutoUpdateFilesImage.setMaxAccess(_A)
if mibBuilder.loadTexts:rlAutoUpdateFilesImage.setStatus(_B)
_RlAutoUpdateFilesConf_Type=TruthValue
_RlAutoUpdateFilesConf_Object=MibScalar
rlAutoUpdateFilesConf=_RlAutoUpdateFilesConf_Object((1,3,6,1,4,1,89,123,4),_RlAutoUpdateFilesConf_Type())
rlAutoUpdateFilesConf.setMaxAccess(_A)
if mibBuilder.loadTexts:rlAutoUpdateFilesConf.setStatus(_B)
_RlAutoUpdateCopyEnable_Type=TruthValue
_RlAutoUpdateCopyEnable_Object=MibScalar
rlAutoUpdateCopyEnable=_RlAutoUpdateCopyEnable_Object((1,3,6,1,4,1,89,123,5),_RlAutoUpdateCopyEnable_Type())
rlAutoUpdateCopyEnable.setMaxAccess(_A)
if mibBuilder.loadTexts:rlAutoUpdateCopyEnable.setStatus(_B)
_RlAutoUpdatePreserveIP_Type=TruthValue
_RlAutoUpdatePreserveIP_Object=MibScalar
rlAutoUpdatePreserveIP=_RlAutoUpdatePreserveIP_Object((1,3,6,1,4,1,89,123,6),_RlAutoUpdatePreserveIP_Type())
rlAutoUpdatePreserveIP.setMaxAccess(_A)
if mibBuilder.loadTexts:rlAutoUpdatePreserveIP.setStatus(_B)
mibBuilder.exportSymbols('RADLAN-AUTOUPDATE-MIB',**{'rlAutoUpdate':rlAutoUpdate,'rlAutoUpdateEnable':rlAutoUpdateEnable,'rlAutoUpdateFilesBoot':rlAutoUpdateFilesBoot,'rlAutoUpdateFilesImage':rlAutoUpdateFilesImage,'rlAutoUpdateFilesConf':rlAutoUpdateFilesConf,'rlAutoUpdateCopyEnable':rlAutoUpdateCopyEnable,'rlAutoUpdatePreserveIP':rlAutoUpdatePreserveIP})