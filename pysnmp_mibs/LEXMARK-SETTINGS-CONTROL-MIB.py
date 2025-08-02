_G='mibLocalizeControl'
_F='mibWalkControl'
_E='read-write'
_D='controlGroup'
_C='Integer32'
_B='current'
_A='LEXMARK-SETTINGS-CONTROL-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lexmarkModules,=mibBuilder.importSymbols('LEXMARK-ROOT-MIB','lexmarkModules')
settingsControl,settingsMIBCompliances,settingsMIBGroups=mibBuilder.importSymbols('LEXMARK-SETTINGS-MIB','settingsControl','settingsMIBCompliances','settingsMIBGroups')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
settingsControlMibModule=ModuleIdentity((1,3,6,1,4,1,641,4,3))
if mibBuilder.loadTexts:settingsControlMibModule.setRevisions(('2014-03-16 12:42',))
class _MibWalkControl_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('none',0),('settingDefinition',1)))
_MibWalkControl_Type.__name__=_C
_MibWalkControl_Object=MibScalar
mibWalkControl=_MibWalkControl_Object((1,3,6,1,4,1,641,7,2,1),_MibWalkControl_Type())
mibWalkControl.setMaxAccess(_E)
if mibBuilder.loadTexts:mibWalkControl.setStatus(_B)
class _MibLocalizeControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_MibLocalizeControl_Type.__name__=_C
_MibLocalizeControl_Object=MibScalar
mibLocalizeControl=_MibLocalizeControl_Object((1,3,6,1,4,1,641,7,2,2),_MibLocalizeControl_Type())
mibLocalizeControl.setMaxAccess(_E)
if mibBuilder.loadTexts:mibLocalizeControl.setStatus(_B)
controlGroup=ObjectGroup((1,3,6,1,4,1,641,7,1,2,1))
controlGroup.setObjects(*((_A,_F),(_A,_G)))
if mibBuilder.loadTexts:controlGroup.setStatus(_B)
controlMIBCompliance=ModuleCompliance((1,3,6,1,4,1,641,7,1,1,1))
controlMIBCompliance.setObjects(*((_A,_D),(_A,_D)))
if mibBuilder.loadTexts:controlMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'settingsControlMibModule':settingsControlMibModule,'controlMIBCompliance':controlMIBCompliance,_D:controlGroup,_F:mibWalkControl,_G:mibLocalizeControl})