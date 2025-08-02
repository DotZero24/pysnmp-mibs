_F='raisecomMultiSysVerIndex'
_E='SWITCH-MULTISYS-MIB'
_D='OctetString'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
raisecomAgent,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','raisecomAgent')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
raisecomMultiSys=ModuleIdentity((1,3,6,1,4,1,8886,1,22))
if mibBuilder.loadTexts:raisecomMultiSys.setRevisions(('2011-01-07 00:00',))
_RaisecomMultiSysMibObjects_ObjectIdentity=ObjectIdentity
raisecomMultiSysMibObjects=_RaisecomMultiSysMibObjects_ObjectIdentity((1,3,6,1,4,1,8886,1,22,1))
_RaisecomMultiSysGlobalGroup_ObjectIdentity=ObjectIdentity
raisecomMultiSysGlobalGroup=_RaisecomMultiSysGlobalGroup_ObjectIdentity((1,3,6,1,4,1,8886,1,22,1,1))
_RaisecomMultiSysVerNum_Type=Unsigned32
_RaisecomMultiSysVerNum_Object=MibScalar
raisecomMultiSysVerNum=_RaisecomMultiSysVerNum_Object((1,3,6,1,4,1,8886,1,22,1,1,1),_RaisecomMultiSysVerNum_Type())
raisecomMultiSysVerNum.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomMultiSysVerNum.setStatus(_A)
_RaisecomMultiSysOverWriteVer_Type=Unsigned32
_RaisecomMultiSysOverWriteVer_Object=MibScalar
raisecomMultiSysOverWriteVer=_RaisecomMultiSysOverWriteVer_Object((1,3,6,1,4,1,8886,1,22,1,1,2),_RaisecomMultiSysOverWriteVer_Type())
raisecomMultiSysOverWriteVer.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomMultiSysOverWriteVer.setStatus(_A)
_RaisecomMultiSysUploadVer_Type=Unsigned32
_RaisecomMultiSysUploadVer_Object=MibScalar
raisecomMultiSysUploadVer=_RaisecomMultiSysUploadVer_Object((1,3,6,1,4,1,8886,1,22,1,1,3),_RaisecomMultiSysUploadVer_Type())
raisecomMultiSysUploadVer.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomMultiSysUploadVer.setStatus(_A)
_RaisecomMultiSysNextBootVer_Type=Unsigned32
_RaisecomMultiSysNextBootVer_Object=MibScalar
raisecomMultiSysNextBootVer=_RaisecomMultiSysNextBootVer_Object((1,3,6,1,4,1,8886,1,22,1,1,4),_RaisecomMultiSysNextBootVer_Type())
raisecomMultiSysNextBootVer.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomMultiSysNextBootVer.setStatus(_A)
_RaisecomMultiSysVerTable_Object=MibTable
raisecomMultiSysVerTable=_RaisecomMultiSysVerTable_Object((1,3,6,1,4,1,8886,1,22,1,2))
if mibBuilder.loadTexts:raisecomMultiSysVerTable.setStatus(_A)
_RaisecomMultiSysVerEntry_Object=MibTableRow
raisecomMultiSysVerEntry=_RaisecomMultiSysVerEntry_Object((1,3,6,1,4,1,8886,1,22,1,2,1))
raisecomMultiSysVerEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:raisecomMultiSysVerEntry.setStatus(_A)
_RaisecomMultiSysVerIndex_Type=Unsigned32
_RaisecomMultiSysVerIndex_Object=MibTableColumn
raisecomMultiSysVerIndex=_RaisecomMultiSysVerIndex_Object((1,3,6,1,4,1,8886,1,22,1,2,1,1),_RaisecomMultiSysVerIndex_Type())
raisecomMultiSysVerIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:raisecomMultiSysVerIndex.setStatus(_A)
class _RaisecomMultiSysVerName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_RaisecomMultiSysVerName_Type.__name__=_D
_RaisecomMultiSysVerName_Object=MibTableColumn
raisecomMultiSysVerName=_RaisecomMultiSysVerName_Object((1,3,6,1,4,1,8886,1,22,1,2,1,2),_RaisecomMultiSysVerName_Type())
raisecomMultiSysVerName.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomMultiSysVerName.setStatus(_A)
_RaisecomMultiSysVerSize_Type=Unsigned32
_RaisecomMultiSysVerSize_Object=MibTableColumn
raisecomMultiSysVerSize=_RaisecomMultiSysVerSize_Object((1,3,6,1,4,1,8886,1,22,1,2,1,3),_RaisecomMultiSysVerSize_Type())
raisecomMultiSysVerSize.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomMultiSysVerSize.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'raisecomMultiSys':raisecomMultiSys,'raisecomMultiSysMibObjects':raisecomMultiSysMibObjects,'raisecomMultiSysGlobalGroup':raisecomMultiSysGlobalGroup,'raisecomMultiSysVerNum':raisecomMultiSysVerNum,'raisecomMultiSysOverWriteVer':raisecomMultiSysOverWriteVer,'raisecomMultiSysUploadVer':raisecomMultiSysUploadVer,'raisecomMultiSysNextBootVer':raisecomMultiSysNextBootVer,'raisecomMultiSysVerTable':raisecomMultiSysVerTable,'raisecomMultiSysVerEntry':raisecomMultiSysVerEntry,_F:raisecomMultiSysVerIndex,'raisecomMultiSysVerName':raisecomMultiSysVerName,'raisecomMultiSysVerSize':raisecomMultiSysVerSize})